document.addEventListener('DOMContentLoaded', () => {
    const syncButton = document.getElementById('sync-button');
    const syncStatus = document.getElementById('sync-status');
    const syncTime = document.getElementById('sync-time');

    syncButton.addEventListener('click', () => {
        syncStatus.textContent = 'Syncing...';
        syncButton.disabled = true;

        fetch('/sync', {
            method: 'POST',
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                syncStatus.textContent = 'Success';
            } else {
                syncStatus.textContent = `Error: ${data.message}`;
            }
            syncTime.textContent = new Date().toLocaleString();
        })
        .catch(error => {
            syncStatus.textContent = `Error: ${error.toString()}`;
            syncTime.textContent = new Date().toLocaleString();
        })
        .finally(() => {
            syncButton.disabled = false;
        });
    });
});
