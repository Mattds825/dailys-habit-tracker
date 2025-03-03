/**
 * Created by Matthew G Da Silva 13/02/2025
 *
 * This script is used to generate the calendar heatmap for the habits.
 * It is used in the user_habits page
 *
 * used chatGPT to generate starter code
 */

const heatmaps = document.getElementsByClassName("calHeatmap");

document.addEventListener("DOMContentLoaded", function () {
  for (let heatmap of heatmaps) {
    // set the default view to month for each heatmap
    setView("month", heatmap.id);
  }
});

/**
 * Sets the view for the calendar heatmap.
 *
 * @param {string} view - The view mode for the calendar (e.g., "monthly", "weekly").
 * @param {string} heatmapId - The ID of the heatmap element.
 */
function setView(view, heatmapId) {
  console.log("setting view", view, heatmapId);

  const heatmap = document.getElementById(heatmapId);

  // get the raw data from the heatmap element
  const rawData = document
    .getElementById(heatmapId)
    .dataset.checkins.split(",");

  const datePattern = /\d{4}-\d{2}-\d{2}/;

  // extract the checkin dates from the raw data
  const checkins = rawData
    .map((entry) => {
      const match = entry.match(datePattern);
      return match ? match[0].split(" ")[0] : null;
    })
    .filter((date) => date !== null);

  // generate the calendar heatmap based on the view
  generateCalendar(view, heatmap, checkins, heatmapId);
}


/**
 * Returns the contribution level for a given date.
 *
 * @param {string} date - The date to check.
 * @param {Array} contributions - The list of contributions.
 * @returns {number} - The contribution level for the date.
 * */
function getContributionLevel(date, contributions) {
  let count = contributions.filter((d) => d === date).length;
  if (count >= 4) return 4;
  if (count === 3) return 3;
  if (count === 2) return 2;
  if (count === 1) return 1;
  return 0;
}


/**
 * Generates a calendar heatmap view based on the specified view type.
 *
 * @param {string} view - The view type for the calendar. Can be "year", "month", or "week".
 * @param {HTMLElement} calendarEl - The HTML element where the calendar will be rendered.
 * @param {Object} contributions - An object containing the contribution data.
 * @param {string} heatmapId - The ID of the heatmap.
 */
function generateCalendar(view, calendarEl, contributions, heatmapId) {
  calendarEl.innerHTML = `
    <div class="cal-controls col-12">
        <div class="btn-group" role="group" aria-label="View Controls">
          <button class="btn btn-secondary btn-sm control-btn ${
            view == "year" ? "disabled" : ""
          }" onclick="setView('year', '${heatmapId}')" >Year</button>
          <button class="btn btn-secondary btn-sm control-btn" ${
            view == "month" ? "disabled" : ""
          } onclick="setView('month', '${heatmapId}')" >Month</button>
          <button class="btn btn-secondary btn-sm control-btn" ${
            view == "week" ? "disabled" : ""
          } onclick="setView('week', '${heatmapId}')" >Week</button>
        </div>
    </div>
  `;

  const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];
  const year = new Date().getFullYear();
  const daysInMonth = [
    31,
    (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0 ? 29 : 28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31,
  ];

  let startMonth = 0,
    endMonth = 12;

  if (view === "month") {
    startMonth = new Date().getMonth();
    endMonth = startMonth + 1;
  } else if (view === "week") {
    const today = new Date();
    const startOfWeek = new Date(today);
    startOfWeek.setDate(today.getDate() - ((today.getDay() + 6) % 7));

    const weekEl = document.createElement("div");
    weekEl.classList.add("days");

    for (let i = 0; i < 7; i++) {
      const date = new Date(startOfWeek);
      date.setDate(startOfWeek.getDate() + i);
      const formattedDate = `${date.getFullYear()}-${String(
        date.getMonth() + 1
      ).padStart(2, "0")}-${String(date.getDate()).padStart(2, "0")}`;

      const dayEl = document.createElement("div");
      dayEl.classList.add("day");
      let level = getContributionLevel(formattedDate, contributions);
      if (level > 0) dayEl.classList.add(`level-${level}`);
      dayEl.setAttribute("data-toggle", "tooltip");
      dayEl.setAttribute("data-placement", "top");
      dayEl.setAttribute("title", `${level} contributions on ${date.toDateString()}`);
      $(dayEl).tooltip();
      weekEl.appendChild(dayEl);
    }

    calendarEl.appendChild(weekEl);
    return;
  }

  for (let i = startMonth; i < endMonth; i++) {
    const monthEl = document.createElement("div");
    monthEl.classList.add("month");
    const monthName = document.createElement("div");
    monthName.classList.add("month-name");
    monthName.textContent = months[i];
    monthEl.appendChild(monthName);

    const daysEl = document.createElement("div");
    daysEl.classList.add("days");
    let daysCount = daysInMonth[i];

    for (let d = 1; d <= daysCount; d++) {
      const date = `${year}-${String(i + 1).padStart(2, "0")}-${String(
        d
      ).padStart(2, "0")}`;
      const dayEl = document.createElement("div");
      dayEl.classList.add("day");
      let level = getContributionLevel(date, contributions);
      if (level > 0) dayEl.classList.add(`level-${level}`);
      dayEl.setAttribute("data-toggle", "tooltip");
      dayEl.setAttribute("data-placement", "top");
      dayEl.setAttribute("title", `${level} contributions on ${date}`);
      $(dayEl).tooltip();
      daysEl.appendChild(dayEl);
    }

    monthEl.appendChild(daysEl);
    calendarEl.appendChild(monthEl);
  }
}
