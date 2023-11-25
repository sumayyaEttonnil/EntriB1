document.addEventListener('DOMContentLoaded', function() {
  // Function to toggle seat layout visibility
  function toggleSeatsBtn(button) {
    const seatLayout = button.nextElementSibling;
    if (seatLayout) {
      if (seatLayout.style.display === 'none' || seatLayout.style.display === '') {
        seatLayout.style.display = 'block';
        button.textContent = 'Hide Seats';
      } else {
        seatLayout.style.display = 'none';
        button.textContent = 'View Seats';
      }
    } else {
      console.error('Seat layout not found');
    }
  }

  // Attach event listeners to all view seat buttons
  const viewSeatButtons = document.querySelectorAll('.toggleSeatsBtn');
  viewSeatButtons.forEach(button => {
    button.addEventListener('click', function() {
      toggleSeatsBtn(this);
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
    }
    updateTotalPrice(seat.closest('.bus-info'));
  }

  function hidePassengerDetailsForm(passengerDetailsForm) {
    passengerDetailsForm.style.display = 'none';
  }

  function redirectToPayment(totalPrice,passengerDetails,busId,date) {
    const encodedPassengerDetails = encodeURIComponent(JSON.stringify(passengerDetails));
    const paymentPageURL = `/payment/?totalPrice=${totalPrice}&passengerDetails=${encodedPassengerDetails}&busId=${busId}&date=${date}`;
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
      console.log('clicked');
      const busIdElement = document.getElementById('busId');
      const busId = busIdElement.textContent;
      const date = document.getElementById('date').innerText;
      console.log(busId)
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
        console.log(passengerDetails)
      });

      if (passengerDetails.length === selectedSeats.length) {



              // Redirect to payment page after the database is updated
              const totalPrice = calculateTotalPrice(passengerDetailsForm.closest('.bus-info'));
              redirectToPayment(totalPrice,passengerDetails,busId,date);
              hidePassengerDetailsForm(passengerDetailsForm);

          };
      })

    const closePassengerDetailsBtn = passengerDetailsForm.querySelector('#closePassengerDetails');
    closePassengerDetailsBtn.addEventListener('click', function() {
      hidePassengerDetailsForm(passengerDetailsForm);
    });
  };

// Rest of your code...

// Add this block to prevent multiple bookings for the same seat
const busInfoElements = document.querySelectorAll('.bus-info');

function seatClickHandler(event) {
  const clickedSeat = event.target.closest('.box');
  if (clickedSeat) {
    if (clickedSeat.classList.contains('available') || clickedSeat.classList.contains('selected')) {
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

      // Disable the click event listener for the selected seat
      clickedSeat.classList.add('booked');
      clickedSeat.removeEventListener('click', seatClickHandler);
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
