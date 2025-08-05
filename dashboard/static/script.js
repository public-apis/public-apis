document.addEventListener('DOMContentLoaded', () => {
    const syncButton = document.getElementById('sync-button');
    const syncStatus = document.getElementById('sync-status');
    const syncTime = document.getElementById('sync-time');
    const nextSyncTime = document.getElementById('next-sync-time');

    function fetchNextSyncTime() {
        fetch('/next-sync-time')
            .then(response => response.json())
            .then(data => {
                if (data.next_run_time) {
                    nextSyncTime.textContent = new Date(data.next_run_time).toLocaleString();
                } else {
                    nextSyncTime.textContent = 'N/A';
                }
            })
            .catch(error => {
                nextSyncTime.textContent = 'Error loading next sync time.';
                console.error('Error fetching next sync time:', error);
            });
    }

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
            fetchNextSyncTime(); // Refresh next sync time after a manual sync
        })
        .catch(error => {
            syncStatus.textContent = `Error: ${error.toString()}`;
            syncTime.textContent = new Date().toLocaleString();
        })
        .finally(() => {
            syncButton.disabled = false;
        });
    });

    // Fetch the next sync time when the page loads
    fetchNextSyncTime();
});
