// Function to handle tab switching
function openTab(event, tabName) {
    // Get all tab content elements and hide them
    const tabContents = document.getElementsByClassName("tab-content");
    for (let content of tabContents) {
        content.classList.remove("active");
    }

    // Remove active class from all tab buttons
    const tabButtons = document.getElementsByClassName("tab-button");
    for (let button of tabButtons) {
        button.classList.remove("active");
    }

    // Show the selected tab content and activate the button
    document.getElementById(tabName).classList.add("active");
    event.currentTarget.classList.add("active");
}

// Function to show BMI information section
function showBMIInfo() {
    const bmiInfo = document.getElementById("bmiInfo");
    if (bmiInfo) {
        bmiInfo.style.display = "block";
        // Ensure the first tab is active by default
        const firstTab = document.querySelector(".tab-button");
        const firstContent = document.querySelector(".tab-content");
        if (firstTab && firstContent) {
            firstTab.classList.add("active");
            firstContent.classList.add("active");
        }
        // Scroll to the BMI info section
        bmiInfo.scrollIntoView({ behavior: "smooth", block: "start" });
    }
}

// Function to hide BMI information section
function hideBMIInfo() {
    const bmiInfo = document.getElementById("bmiInfo");
    if (bmiInfo) {
        bmiInfo.style.display = "none";
    }
}

// Event listener for form submission
document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("bmi-form");
    const resetButton = document.getElementById("reset-button");

    if (form) {
        form.addEventListener("submit", function(event) {
            // The form will be handled by Flask, but we want to show the BMI info
            // after the page reloads if there's a result
            if (document.getElementById("bmi-result")) {
                showBMIInfo();
            }
        });
    }

    // Hide BMI info when reset button is clicked
    if (resetButton) {
        resetButton.addEventListener("click", function() {
            hideBMIInfo();
        });
    }

    // Show BMI info on page load if there's a result
    if (document.getElementById("bmi-result")) {
        showBMIInfo();
    }
});
