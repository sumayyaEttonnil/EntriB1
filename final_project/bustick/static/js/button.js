document.addEventListener('DOMContentLoaded', function() {
  const bookButtons = document.querySelectorAll('.bookButton');

  bookButtons.forEach(bookButton => {
    bookButton.addEventListener('click', function() {
      const selectedSeats = this.closest('.bus-info').querySelectorAll('.selected');

      if (selectedSeats.length === 0) {
        // If no seats are selected, alert the user to select at least one seat
        alert('Please select at least one seat for booking.');
      } else {
        // If seats are selected, display the passenger details form
        const passengerDetailsForm = this.closest('.bus-info').querySelector('.passengerDetailsForm');
        passengerDetailsForm.style.display = 'block';

        // Clear previous passenger details
        const passengerDetailsDiv = passengerDetailsForm.querySelector('#passengerDetails');
        passengerDetailsDiv.innerHTML = '';

        // Add input fields for each selected seat's passenger details
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

        // Handle the form submission or other actions here
        const submitPassengerDetailsBtn = passengerDetailsForm.querySelector('#submitPassengerDetails');
        submitPassengerDetailsBtn.addEventListener('click', function() {
          // Get passenger details
          const passengerContacts = document.querySelectorAll('[id^=passengerName]');
          const passengerDetails = [];
          let invalidField = false;

          passengerContacts.forEach(passengerContact => {
            const passengerName = document.getElementById(passengerContact.id).value.trim();
            const seatNumber = passengerContact.id.split('_')[1];
            const passengerGender = document.getElementById(`passengerGender_${seatNumber}`).value;

            if (!passengerName) {
              invalidField = true;
              alert(`Please fill in the Name for Seat ${seatNumber}.`);
            } else {
              passengerDetails.push({ seatNumber, passengerName, passengerGender });
            }
          });

          if (invalidField) {
            // If any field is invalid, prevent form submission
            return;
          }

          // Get the shared contact number
          const sharedContact = document.getElementById('sharedContact').value.trim();

          if (!sharedContact) {
            alert('Please provide the Shared Contact.');
            return;
          }

          // Process passenger details or perform other actions
          console.log('Passenger Details:', passengerDetails);
          console.log('Shared Contact:', sharedContact);

          // Close the passenger details form after submission
          passengerDetailsForm.style.display = 'none';
        });

        // Close passenger details form when close button is clicked
        const closePassengerDetailsBtn = passengerDetailsForm.querySelector('#closePassengerDetails');
        closePassengerDetailsBtn.addEventListener('click', function() {
          passengerDetailsForm.style.display = 'none';
        });
      }
    });
  });
});
