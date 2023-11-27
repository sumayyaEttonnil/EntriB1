document.addEventListener('DOMContentLoaded', function() {

  // Function to toggle seat layout visibility
  function toggleSeatsBtn(button) {
    const seatLayout = button.nextElementSibling;
    const legend = seatLayout.querySelector('.legend'); // Selecting the legend

    if (seatLayout) {
      if (seatLayout.style.display === 'none' || seatLayout.style.display === '') {
        seatLayout.style.display = 'block';
        legend.style.display = 'block'; // Show the legend
        button.textContent = 'Hide Seats';
      } else {
        seatLayout.style.display = 'none';
        legend.style.display = 'none'; // Hide the legend
        button.textContent = 'View Seats';
      }
    } else {
      console.error('Seat layout not found');
    }
  }

  // Function to fetch booked seats for a specific bus ID
  function fetchBookedSeats(busId, date,busName) {
    // Make a GET request to your backend API endpoint
    fetch(`/backend_booking_endpoint/?busId=${busId}&date=${date}`, {
      method: 'GET',
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch booked seats');
        }
        return response.json();
      })
      .then(data => {
        console.log('Booked seats data:', data); // Log retrieved booked seats data

        // Process the response data (booked seat numbers)
        const bookedSeats = data.booked_seats; // Adjust the response structure based on your API

        // Iterate through each booked seat and update their appearance
        bookedSeats.forEach(seatNumber => {
          const seat = seatNumber.seat_number
          const seatElement = document.querySelector(`[data-seat-number="${seat}"][data-bus-id="${busId}"]`);
          if (seatElement) {
            seatElement.closest('.box').classList.remove('available');
            seatElement.closest('.box').classList.add('booked');
            // Disable the click event listener for the booked seat
            seatElement.closest('.box').removeEventListener('click', seatClickHandler);
          }
        });
      })
      .catch(error => {
        console.error('Error fetching booked seats:', error);
        // Handle the error scenario
      });
  }

  // Attach event listeners to all view seat buttons
  const viewSeatButtons = document.querySelectorAll('.toggleSeatsBtn');
  viewSeatButtons.forEach(button => {
    button.addEventListener('click', function() {
      toggleSeatsBtn(this);

      const busId = this.parentElement.querySelector('#busId').textContent;
      const busNameElement1 = document.getElementById('busName');
      const busName = busNameElement1.textContent.trim();
      //console.log(busName);

      const date_input = document.getElementById('date').innerText;
      // Split the date string into day, month, and year
      const [day, month, year] = date_input.split('-');
      // Rearrange the components to form the desired date format (YYYY-MM-DD)
      const date = `${year}-${month}-${day}`;

      console.log(`Bus ID: ${busId}, Date: ${date},busName:${busName}`); // Log bus ID and date

      // Call the function to fetch booked seats for the selected bus ID
      fetchBookedSeats(busId, date,busName);
    });
  });

  // Function to toggle seat color
  function toggleSeatColor(seat) {
    if (seat.classList.contains('available')) {
      seat.classList.remove('available');
      seat.classList.add('selected');
    } else if (seat.classList.contains('selected')) {
      seat.classList.remove('selected');
      seat.classList.add('available');
    } else if (seat.classList.contains('booked')) {
    // Handle the scenario where a booked seat is clicked (optional)
    console.log('This seat is already booked and cannot be selected.');
    }
    updateTotalPrice(seat.closest('.bus-info'));
  }

  function hidePassengerDetailsForm(passengerDetailsForm) {
    passengerDetailsForm.style.display = 'none';
  }

  function redirectToPayment(totalPrice, passengerDetails, busId, date,busName) {
    const encodedPassengerDetails = encodeURIComponent(JSON.stringify(passengerDetails));
    const paymentPageURL = `/payment/?totalPrice=${totalPrice}&passengerDetails=${encodedPassengerDetails}&busId=${busId}&date=${date}&busName=${busName}`;
    window.location.href = paymentPageURL;
  }

  function displayPassengerDetailsForm(selectedSeats, passengerDetailsForm) {
    const passengerDetailsDiv = passengerDetailsForm.querySelector('#passengerDetails');
    passengerDetailsDiv.innerHTML = ''; // Clear previous passenger details

    selectedSeats.forEach(seat => {
      const passengerDetailInputs = `
        <div>
          <label for="passengerName_${seat.textContent}">Name (${seat.textContent}):</label>
          <input type="text" id="passengerName_${seat.textContent}" name="passengerName_${seat.textContent}" required><br><br>
          <label for="passengerGender_${seat.textContent}">Gender (${seat.textContent}):</label>
          <select id="passengerGender_${seat.textContent}" name="passengerGender_${seat.textContent}" required>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
          </select><br><br>
        </div>
      `;
      passengerDetailsDiv.innerHTML += passengerDetailInputs;
    });

    passengerDetailsForm.style.display = 'block';

    const proceedToPayBtn = passengerDetailsForm.querySelector('#proceedToBook');
    proceedToPayBtn.addEventListener('click', function() {
      const busIdElement = document.getElementById('busId');
      const busNameElement = document.getElementById('busName');
      const busId = busIdElement.textContent;
      const date = document.getElementById('date').innerText;
      const busName = busNameElement.textContent;
      const passengerDetails = [];

      selectedSeats.forEach(seat => {
        const passengerName = document.getElementById(`passengerName_${seat.textContent}`).value.trim();
        const seatNumber = seat.textContent;
        const passengerGender = document.getElementById(`passengerGender_${seat.textContent}`).value;
        if (!passengerName || !passengerGender) {
          alert('Please fill in all passenger details.');
          return;
        }

        passengerDetails.push({ seatNumber, passengerName, passengerGender });
      });

      if (passengerDetails.length === selectedSeats.length) {
        const totalPrice = calculateTotalPrice(passengerDetailsForm.closest('.bus-info'));
        redirectToPayment(totalPrice, passengerDetails, busId, date,busName);
        hidePassengerDetailsForm(passengerDetailsForm);
      }
    });

    const closePassengerDetailsBtn = passengerDetailsForm.querySelector('#closePassengerDetails');
    closePassengerDetailsBtn.addEventListener('click', function() {
      hidePassengerDetailsForm(passengerDetailsForm);
    });
  }

  // Add this block to prevent multiple bookings for the same seat
  const busInfoElements = document.querySelectorAll('.bus-info');

  // Event listener for seat selection
function seatClickHandler(event) {
  const clickedSeat = event.target.closest('.box');
  if (clickedSeat) {
    if (clickedSeat.classList.contains('selected')) {
      // If the seat is already selected, toggle it back to available and update UI
      toggleSeatColor(clickedSeat);
      const updatedBusInfo = clickedSeat.closest('.bus-info');
      updateTotalPrice(updatedBusInfo);

      const selectedSeats = updatedBusInfo.querySelectorAll('.selected');
      const passengerDetailsForm = updatedBusInfo.querySelector('.passengerDetailsForm');

      if (selectedSeats.length > 0) {
        displayPassengerDetailsForm(selectedSeats, passengerDetailsForm);
      } else {
        hidePassengerDetailsForm(passengerDetailsForm);
      }
    } else if (clickedSeat.classList.contains('available')) {
      // If the seat is available, mark it as selected
      toggleSeatColor(clickedSeat);
      const updatedBusInfo = clickedSeat.closest('.bus-info');
      updateTotalPrice(updatedBusInfo);

      const selectedSeats = updatedBusInfo.querySelectorAll('.selected');
      const passengerDetailsForm = updatedBusInfo.querySelector('.passengerDetailsForm');

      if (selectedSeats.length > 0) {
        displayPassengerDetailsForm(selectedSeats, passengerDetailsForm);
      } else {
        hidePassengerDetailsForm(passengerDetailsForm);
      }
    } else if (clickedSeat.classList.contains('booked')) {
      // Handle the scenario where a booked seat is clicked (optional)
      console.log('This seat is already booked and cannot be selected.');
    }
  }
}


  busInfoElements.forEach(busInfoElement => {
    const seatContainers = busInfoElement.querySelectorAll('.seat-container');
    seatContainers.forEach(container => {
      container.addEventListener('click', seatClickHandler);
    });
  });

  function calculateTotalPrice(busInfoElement) {
    let totalPrice = 0;
    const pricePerSeat = parseFloat(busInfoElement.querySelector('.priceValue').getAttribute('data-price'));
    const selectedSeats = busInfoElement.querySelectorAll('.selected');
    totalPrice = pricePerSeat * selectedSeats.length;
    return totalPrice;
  }

  function updateTotalPrice(busInfoElement) {
    const totalPriceElement = busInfoElement.querySelector('.booking-section #totalPrice');
    const totalPrice = calculateTotalPrice(busInfoElement);
    totalPriceElement.textContent = totalPrice;
  }

  busInfoElements.forEach(busInfoElement => {
    updateTotalPrice(busInfoElement);
  });
});
