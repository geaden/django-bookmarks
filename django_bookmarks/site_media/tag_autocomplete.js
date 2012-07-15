$(document).ready(funciton () {
   $("#id_tags").autocomplete(
   '/ajax/tag/autocomplete/',
    {multiple: true, multipleSeparator: ' '}
    );
});
