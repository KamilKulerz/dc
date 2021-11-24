  function openModal(button) {
      document.getElementById("#modalLink").href = button.getAttribute('data-url')
      $("#exampleModalCenter").modal("show");
  }

  function openModalClear(button) {
      document.getElementById("#modalLinkClear").href = button.getAttribute('data-url')
      $("#exampleModalCenterClear").modal("show");
  }

  function closeModal() {
      document.getElementById("exampleModalCenter").style.display = "none"
      document.getElementById("exampleModalCenter").classList.remove("show")
  }
  // Get the modal
  var modal = document.getElementById('exampleModal');

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
      if (event.target == modal) {
          closeModal()
      }
  }