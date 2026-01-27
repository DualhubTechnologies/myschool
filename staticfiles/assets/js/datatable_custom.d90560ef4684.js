  document.addEventListener("DOMContentLoaded", function () {
    if (window.jQuery && $.fn.DataTable) {
        $('.schltb').DataTable({
            pageLength: 7,
            lengthChange: true,
            searching: true,
            ordering: true,
            responsive: true,
            columnDefs: [
                { orderable: false, targets: -1 } // Disable sorting on Actions
            ]
        });
    }
});