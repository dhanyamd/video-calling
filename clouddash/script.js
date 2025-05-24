// Navigation functionality
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link');
    const pages = document.querySelectorAll('.page');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Remove active class from all links and pages
            navLinks.forEach(l => l.classList.remove('active'));
            pages.forEach(p => p.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
            
            // Show corresponding page
            const pageId = this.getAttribute('data-page');
            document.getElementById(pageId).classList.add('active');
        });
    });
});


// Widget configuration functionality
function showWidgetMenu(button) {
    const widget = button.closest('.widget');
    if (widget.id === 'broken-widget') {
        document.getElementById('widget-modal').style.display = 'flex';
    } else {
        alert('Widget configuration would open here for working widgets.');
    }
}

function closeModal() {
    document.getElementById('widget-modal').style.display = 'none';
}

function updateWidget() {
    const refreshRate = document.getElementById('widget-refresh-rate').value;
    
    if (refreshRate === '5min' || refreshRate === '15min') {
        // Fix the widget by updating refresh rate
        const brokenWidget = document.getElementById('broken-widget');
        brokenWidget.querySelector('.widget-error').style.display = 'none';
        brokenWidget.querySelector('.widget-content').innerHTML = `
            <div class="chart-placeholder">
                <div class="bar" style="height: 85%"></div>
                <div class="bar" style="height: 70%"></div>
                <div class="bar" style="height: 90%"></div>
                <div class="bar" style="height: 65%"></div>
            </div>
            <p style="margin-top: 1rem; color: #4CAF50; font-weight: 600;">Widget updated! Refresh rate: ${refreshRate === '5min' ? '5 minutes' : '15 minutes'}</p>
        `;
        brokenWidget.classList.remove('error');
        closeModal();
        alert('Widget updated successfully! Data is now loading properly.');
    } else if (refreshRate === '1min') {
        alert('1 minute refresh rate requires Premium subscription. Please select 5 minutes or higher.');
    } else {
        alert('1 hour refresh rate is too low for real-time data. Please select 5 or 15 minutes for better performance.');
    }
}

// Export functionality with intentional issues
function exportData() {
    const dataset = document.getElementById('dataset-select').value;
    const format = document.querySelector('input[name="format"]:checked').value;
    
    // Hide error message first
    document.getElementById('export-error').style.display = 'none';
    
    // Simulate size exceeded error for datasets over 10,000 rows in CSV format
    if ((dataset.includes('25,000') || dataset.includes('45,000')) && format === 'csv') {
        // Too many rows for CSV - this is our main demo scenario
        document.getElementById('export-error').style.display = 'block';
        return;
    }
    
    // Success case - export works for XLSX or smaller datasets
    alert('Export started successfully! You will receive a notification when the export is ready to download.');
}

// Add some dynamic behavior to make it feel more realistic
document.addEventListener('DOMContentLoaded', function() {
    // Add hover effects to charts
    const bars = document.querySelectorAll('.bar');
    bars.forEach(bar => {
        bar.addEventListener('mouseenter', function() {
            this.style.transform = 'scaleY(1.1)';
        });
        
        bar.addEventListener('mouseleave', function() {
            this.style.transform = 'scaleY(1)';
        });
    });
    
    // Click outside modal to close
    window.addEventListener('click', function(e) {
        const modal = document.getElementById('widget-modal');
        if (e.target === modal) {
            closeModal();
        }
    });
});


