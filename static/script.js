lucide.createIcons();

      // Logika Loading saat Submit
      const form = document.getElementById("downloadForm");
      const btn = document.getElementById("submitBtn");
      const btnText = document.getElementById("btnText");
      const btnIcon = document.getElementById("btnIcon");
      const spinner = document.getElementById("spinner");

      form.onsubmit = () => {
        btn.disabled = true;
        btn.classList.add("opacity-75", "cursor-not-allowed");
        btnText.innerText = "Memproses...";
        btnIcon.classList.add("hidden");
        spinner.classList.remove("hidden");
      };