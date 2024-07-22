function copyInviteLink(link) {
    navigator.clipboard.writeText(link)
        .then(() => {
            console.log('Invite link copied to clipboard!');
            alert('Invite link copied to clipboard!');
        })
        .catch(err => {
            console.error('Could not copy text:', err);
            alert('Could not copy text: ' + err);
        });
}