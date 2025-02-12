// Function to copy text to clipboard
async function copyToClipboard() {
    var copyText = document.getElementById("shortUrl").textContent;
    try {
        await navigator.clipboard.writeText(copyText);
        alert("Copied: " + copyText);
    } catch (err) {
        console.error('Could not copy text: ', err);
    }
}