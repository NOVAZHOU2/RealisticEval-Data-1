/*
* function generated by ChatGPT
* as a senior javascript developer write a function to calculate how many years, months, days, hours and minutes
* have passed since the birthdate until now. return an array of numbers representing years, months, days, hours and
* minutes. these numbers should not be negative, and less than the next unit, for example, days could not be bigger
* than 31
* */
export function getTimeSinceBornUntilNow(birthDate: Date) {
    const now = new Date();
  
    // Calculate years
    let years = now.getFullYear() - birthDate.getFullYear();
  
    // Calculate months
    let months = now.getMonth() - birthDate.getMonth();
    if (months < 0) {
      years -= 1;
      months += 12;
    }
  
    // Calculate days
    let days = now.getDate() - birthDate.getDate();
    if (days < 0) {
      months -= 1;
      const tempDate = new Date(birthDate);
      tempDate.setMonth(birthDate.getMonth() + 1);
      // @ts-ignore
      days += (now - tempDate) / (1000 * 60 * 60 * 24);
    }
  
    // Calculate hours
    let hours = now.getHours() - birthDate.getHours();
    if (hours < 0) {
      days -= 1;
      hours += 24;
    }
  
    // Calculate minutes
    let minutes = now.getMinutes() - birthDate.getMinutes();
    if (minutes < 0) {
      hours -= 1;
      minutes += 60;
    }
  
    return [years, months, days, hours, minutes];
  }