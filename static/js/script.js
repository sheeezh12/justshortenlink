$(document).ready(function () {
    $("#expire-date").datepicker({
      format: "mm/dd/yyyy",      
      autoclose: true,
      todayHighlight: true
    });


}); 
function showLinkResult(origin, shortCode) {
  const shortLink = `http://127.0.0.1:5000//${shortCode}`;
  document.getElementById("origin_link").textContent = origin;
  document.getElementById("short_link").textContent = shortLink;
  document.getElementById("short_link").href = shortLink;
  document.getElementById("visit_button").href = shortLink;
  document.getElementById("link_result").style.display = "block";
}

function copyToClipboard() {
  const shortLink = document.getElementById("short_link").textContent;
  navigator.clipboard.writeText(shortLink)
    .then(() => alert("Link berhasil disalin 📋"))
    .catch(err => alert("Gagal menyalin link"));
}

function copyToClipboard() {
  navigator.clipboard.writeText(document.getElementById("short_link").textContent)
    .then(() => alert("Link berhasil disalin!"))
    .catch(() => alert("Gagal menyalin link."));
}