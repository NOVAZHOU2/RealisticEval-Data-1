function getRelativeTime(messageDate) {
    const now = new Date();
    const timeDifference = now.getTime() - messageDate.getTime();

    const oneDay = 1000 * 60 * 60 * 24; // milliseconds in one day
    const daysDifference = Math.floor(timeDifference / oneDay);

    if (daysDifference === 0) {
        return "Today";
    } else if (daysDifference === 1) {
        return "Yesterday";
    } else if (daysDifference < 7) {
        const daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
        return daysOfWeek[messageDate.getDay()];
    } else {
        const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
        return messageDate.toLocaleDateString(undefined, options);
    }
}