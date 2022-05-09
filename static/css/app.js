let navigation = document.querySelector('.navigation'); 
let background = document.querySelector('.background');

document.addEventListener('click', (e) =>{  
    console.log(e.composedPath())
});


let dateNow = new Date(),
    nowMonth = dateNow.getMonth(),
    nowYear = dateNow.getFullYear(),
    nowDateNumber = dateNow.getDate(),

    calendar = document.getElementById('calendar'),
    nameMonth = calendar.getElementsByClassName('nameMonth')[0],
    nameYear = calendar.getElementsByClassName('nameYear')[0],
    daysCont = calendar.getElementsByClassName('days')[0],

    monthName = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'];


function setMonthCalendar(year,month) {
    let monthDays = new Date(year, month + 1, 0).getDate(),
        monthPrefix = new Date(year, month, 0).getDay(),
        monthDaysText = '';
    
    
    nameMonth.textContent = monthName[month];
    nameYear.textContent = year;
    daysCont.innerHTML = '';

    // если месяц начинается не с пн создаются пустые даты
    if (monthPrefix >0){
        for (let i = 1; i<= monthPrefix; i++){
            monthDaysText += '<li></li>';
        }
    }

    for (let i = 1; i <= monthDays; i++){
        monthDaysText += '<li>' + i + '</li>';
    }

    daysCont.innerHTML = monthDaysText;

    // помечаем сегодня
    if (month == nowMonth && year == nowYear){
        days = daysCont.getElementsByTagName('li');
        days[monthPrefix + nowDateNumber - 1].classList.add('date-now');
    }

}

setMonthCalendar(nowYear,nowMonth);