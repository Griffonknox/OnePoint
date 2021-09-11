function table_toggle (onclick, table_id, table_alter) {
    $('.' + onclick).click(function() {

    if($("#" + table_id).css('display') == 'none')
    {
        $("#" + table_id).show();
        $("#" + table_alter).hide();
    } else {
        $("#" + table_id).hide();
        $("#" + table_alter).show();
    }

    });
};