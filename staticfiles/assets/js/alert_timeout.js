    document.addEventListener("DOMContentLoaded", function () {
        const alerts = document.querySelectorAll(".flash-message");

        alerts.forEach(function (alert) {
            setTimeout(function () {
                alert.classList.add("fade-out");
                setTimeout(() => alert.remove(), 500);
            }, 1000); // 1 seconds
        });
    });