// 1️⃣ App Settings
const appSettings = {
    appTheme: 'light',
    appSidebar: 'full',
    appColor: 'blue',
};

// 4️⃣ Apply settings
function applySettings() {
    const themeCheckbox = document.getElementById('theme_direction');

    // Theme
    document.documentElement.setAttribute("data-bs-theme", appSettings.appTheme);

    // Sidebar
    if (window.innerWidth >= 1191) {
        document.documentElement.setAttribute("data-app-sidebar", appSettings.appSidebar);
    }

    document.documentElement.setAttribute("data-color-theme", appSettings.appColor);
}


// 6️⃣ Initialize
document.addEventListener("DOMContentLoaded", applySettings);
