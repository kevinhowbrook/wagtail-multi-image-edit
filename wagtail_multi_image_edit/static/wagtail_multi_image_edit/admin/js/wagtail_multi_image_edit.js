var updateEditButton = function (newState) {
    var anySelected = Object.values(newState).some(Boolean);
    var ids = $.map(newState, (value, id) => value ? id : null);
    var $editButton = $('a.button.edit-button');
    $editButton.attr('href', $editButton.data('url') + $.param({id: ids}, true));
    $editButton.toggleClass('visuallyhidden', !anySelected);
}

var buildSelectedState = function () {
    // prepare the selected state -- {3: true, 4: false}
    state = {};
    $rows = $('ul.multi-image-edit li input[type=checkbox].toggle-select-row');
    $.each($rows, function (index, row) {
        var $row = $(row);
        var selected = $row.prop('checked');
        var id = $row.attr('value');
        state[id] = selected;
    });
    return state;
};

var updateSelectedState = function (state, newValue, idToUpdate) {
    if (idToUpdate === null) {
        // update all rows
        $.each(state, function (id, currentValue) {
            state[id] = newValue;
        });
    } else {
        // update single row
        $row = $('ul.multi-image-edit li#image-row-' + idToUpdate);
        $row.toggleClass('selected')
        state[idToUpdate] = newValue;
    }
    return state;
};

var updateView = function (newState) {
    // update the delete button
    updateEditButton(newState);
};

var multiEditForm = function () {
    function ajaxifyForm(form) {
        $(form).on('submit', function (event) {
            event.preventDefault();

            $.ajax({
                type: "POST",
                url: this.action,
                data: $(this).serialize(),
                success: function (data) {
                    console.log(this)
                    if (data.success) {
                        addMessage('success', 'Image Updated');
                        $(form).closest('li').slideUp(function() {$(form).remove();});
                    } else {
                        // validation error - show re-rendered form in place of original
                        var newForm = $(data.form);
                        $(form).replaceWith(newForm);
                        ajaxifyForm(newForm);
                    }
                }
            });
        });
    }

    $('.multi-image-edit-form').each(function() {
        ajaxifyForm(this);
    });
};
$(document).ready(multiEditForm);
$(document).ready(function(){
    $('ul.multi-image-edit').on('click', 'input[type="checkbox"]', function (event) {
        var $target = $(event.target);
        var setToValue = $target.prop('checked');
        var currentState = buildSelectedState();
        var id = null;
        if ($target.hasClass('toggle-select-row')) {
            id = $target.attr('value');
        }
        var newState = updateSelectedState(currentState, setToValue, id);
        updateView(newState);
    });
})
