function animateNumber(targetNumber, elementId, duration) {
    const numberDisplay = document.getElementById(elementId);
    const framesPerSecond = 60;
  
    let currentNumber = 0;
    let animationInterval;
  
    function updateNumber() {
      currentNumber ++;
      if (currentNumber >= targetNumber) {
        clearInterval(animationInterval);
        currentNumber = targetNumber;
      }
      numberDisplay.textContent = Math.round(currentNumber);
    }
  
    animationInterval = setInterval(updateNumber, 1000 / framesPerSecond);
  }

  document.addEventListener("DOMContentLoaded", function () {
    animateNumber(65, "uniqueVisitors", 3000);
  });
  