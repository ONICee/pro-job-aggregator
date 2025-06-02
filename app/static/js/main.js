async function fetchJobs() {
  const keyword = document.getElementById("keyword").value.toLowerCase();
  const category = document.getElementById("category").value;
  const jobsContainer = document.getElementById("jobs-container");
  const loading = document.getElementById("loading");

  // Show loading spinner
  loading.classList.remove("d-none");
  jobsContainer.innerHTML = "";

  try {
    const res = await fetch("/api/jobs?limit=50&page=1");
    const data = await res.json();
    let jobs = data.jobs;

    // Filter by keyword
    if (keyword) {
      jobs = jobs.filter(job =>
        job.title.toLowerCase().includes(keyword) ||
        job.company.toLowerCase().includes(keyword)
      );
    }

    // Filter by category
    if (category) {
      jobs = jobs.filter(job => job.source === category);
    }

    // Render job cards
    if (jobs.length === 0) {
      jobsContainer.innerHTML = "<p class='text-danger'>No jobs found.</p>";
    } else {
      jobs.forEach(job => {
        const card = document.createElement("div");
        card.className = "col-md-6";
        card.innerHTML = `
          <div class="card h-100 shadow-sm">
            <div class="card-body">
              <h5 class="card-title">${job.title}</h5>
              <h6 class="card-subtitle mb-2 text-muted">${job.company}</h6>
              <p class="card-text"><strong>Source:</strong> ${job.source}</p>
              <a href="/job/${job.id}" class="btn btn-outline-primary">View Job</a>
            </div>
          </div>
        `;
        jobsContainer.appendChild(card);
      });
    }
  } catch (error) {
    jobsContainer.innerHTML = "<p class='text-danger'>Error loading jobs.</p>";
  }

  // Hide spinner
  loading.classList.add("d-none");
}


// Initial load
window.onload = fetchJobs;
