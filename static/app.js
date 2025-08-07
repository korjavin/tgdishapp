document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendar');
    const today = new Date();
    let currentMonth = today.getMonth();
    let currentYear = today.getFullYear();

    function renderCalendar(year, month) {
        calendarEl.innerHTML = ''; // Clear previous calendar
        const monthNames = ["January", "February", "March", "April", "May", "June",
                            "July", "August", "September", "October", "November", "December"];

        // Header
        const header = document.createElement('div');
        header.className = 'calendar-header';
        header.innerHTML = `<h2>${monthNames[month]} ${year}</h2>`;
        calendarEl.appendChild(header);

        const daysOfWeek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        daysOfWeek.forEach(day => {
            const dayHeader = document.createElement('div');
            dayHeader.className = 'day-header';
            dayHeader.textContent = day;
            calendarEl.appendChild(dayHeader);
        });

        const firstDay = new Date(year, month).getDay();
        const daysInMonth = 32 - new Date(year, month, 32).getDate();

        for (let i = 0; i < firstDay; i++) {
            const emptyCell = document.createElement('div');
            emptyCell.className = 'day';
            calendarEl.appendChild(emptyCell);
        }

        for (let i = 1; i <= daysInMonth; i++) {
            const dayCell = document.createElement('div');
            dayCell.className = 'day';
            dayCell.textContent = i;
            if (i === today.getDate() && year === today.getFullYear() && month === today.getMonth()) {
                dayCell.classList.add('today');
            }
            calendarEl.appendChild(dayCell);
        }

        fetchDuties(year, month);
    }

    function fetchDuties(year, month) {
        fetch(`/api/duties/${year}/${month + 1}`) // API month is 1-based
            .then(response => response.json())
            .then(duties => {
                duties.forEach(duty => {
                    const dutyDate = new Date(duty.date);
                    const day = dutyDate.getDate();
                    const dayCell = calendarEl.querySelector(`.day:nth-child(${day + new Date(year, month).getDay() + 7})`); // +7 to account for day headers
                    if (dayCell) {
                        const dutyEl = document.createElement('div');
                        dutyEl.className = 'duty';
                        dutyEl.textContent = duty.user.username;
                        dayCell.appendChild(dutyEl);
                    }
                });
            });
    }

    renderCalendar(currentYear, currentMonth);
});
