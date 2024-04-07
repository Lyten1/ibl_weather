<template>
    <div class="main">
        <div class="container">
            <Header/>
            <div class="weather-section">
                <div v-if="activeCardIndex==null" class="forecast-part">
                    <div class="current-day__info">
                        <div class="weather-temperature">
                            <img  class = "current-day__icon" src="/forecast/sunny.svg" alt="">
                            <div class="current-day__temp">
                                <span class="temperature">18</span>
                                °C
                            </div>
                        </div>
                        <div class="current-date-place">
                            <div class="current-date"><span class="current-week-day">Today, </span>06.04</div>
                            <div class="current-place">Abudant sunshine</div>
                        </div>
                    </div>
                    <div class="graphic-section">
                        <div class="graphic-categories">
                            <div class="graphic-category active-graphic-category">Tempreture</div>
                            <div class="graphic-category">Humidity</div>
                            <div class="graphic-category">Wind</div> 
                        </div>
                        <div class="graphic-impl">
                            <div
                                v-for="(bar, i) in normalizeGraph()"
                                :style="{ height: `${bar}%` }"
                                :key="i"
                                class="graphic-column"
                            >
                                <div class="value">{{ this.graph[this.activeDayIndex - 1][i]  + "°"}}</div>
                                <div class="date">{{ i + 10 + ".04" }}</div>   
                            </div>
                        </div>
                    </div>
                    <div class="day-section">
                        <div v-for="index in 8" 
                            :key = "index"
                            class="day-card" 
                            :class="{ 'active-card': this.activeDayIndex === index }"
                            @click="setActiveDay(index)">
                            <div class="week-day">Mon</div>
                            <img src="/forecast/sunny.svg"  alt="" class="day-pic">
                            <div class="day-temp">
                                <span class="max-temp">18° </span>
                                <span class="min-temp">9°</span>
                            </div>
                        </div>
                    
                    </div>
                </div>
                <div v-else class="forecast-part">
                    <div class="forecast-header">
                        <img class="current-day__icon forecast-logo" :src="alertCards['card' + (activeCardIndex+ 1)].urlPhoto" alt="">
                        <div class="forecast-header__content current-date">{{ alertCards['card' + (activeCardIndex+ 1)].message }}</div>
                    </div>
                    <div class="forecast-text" >
                        Attention: Extreme heatwave warning in effect! Anticipate temperatures exceeding 30°C today. <br><br>

Take necessary precautions to safeguard against heat-related illnesses. Stay hydrated by drinking plenty of water, seek shade or air-conditioned environments, and refrain from outdoor activities during peak heat hours.<br><br>

Wear lightweight, loose-fitting clothing and apply sunscreen regularly if venturing outdoors. Keep a close eye on vulnerable individuals such as the elderly, children, and pets, ensuring they stay cool and hydrated. <br><br>

Stay informed through local weather updates and heed any advisories issued by authorities. Let's prioritize safety and well-being during this intense heatwave.<br><br>
                    </div>
                </div>
                <div class="message-part">
                    <div 
                        v-for="(card, obj, idx) in alertCards"
                        :key="idx"
                        @click="setActiveCard(idx)"
                        class="alert-block"
                        :class="{ 'active-card': this.activeCardIndex == idx }"
                    >
                        <img style="background-color: transparent;" class = "alert-icon" :src="card.urlPhoto" alt="">
                        <div class="text-block">
                            <div class="offer__title" :class="{'red-text' : card.warning}">{{ card.message }}</div>
                            <div class="offer__text blue-text">See more...</div>
                        </div>
                        <div class="time-block offer-text">{{card.time}}</div>
                    </div>
                    
                    <div class="more-records-card">More records....</div>
                </div>                
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
export default {
    name: "weatherAI",
    data() {
        return{
            activeDayIndex: 1,
            activeCardIndex: null,
            graph: [
                [100, 18, 19, 60, 15, 23, 12, 17, 17, 18, 19, 26, 15, 23, 12],
                [1, 18, 19, 60, 15, 23, 12, 17, 17, 18, 19, 26, 15, 23, 12],
                [2, 18, 19, 60, 15, 23, 12, 17, 17, 18, 19, 26, 15, 23, 12],
                [3, 18, 19, 60, 15, 23, 12, 17, 17, 18, 19, 26, 15, 23, 12], 
                [4, 18, 19, 60, 15, 23, 12, 17, 17, 18, 19, 26, 15, 23, 12],
                [5, 18, 19, 60, 15, 23, 12, 17, 17, 18, 19, 26, 15, 23, 12],
                [6, 18, 19, 60, 15, 23, 12, 17, 17, 18, 19, 26, 15, 23, 12],
                [100, 18, 19, 60, 15, 23, 12, 17, 17, 18, 19, 26, 15, 23, 12]
            ],

            days: {

            },

            alertCards: {
                card1: {
                    urlPhoto: "/forecast/sunny.svg",
                    message: "Be carefull on sun today!",
                    warning: false,
                    time: "8m ago",
                    text: "Attention: \n Extreme heatwave warning  in effect! Anticipate temperatures exceeding 30°C today. Take necessary precautions to safeguard against heat-related illnesses. Stay hydrated by drinking plenty of water, seek shade or air-conditioned environments, and refrain from outdoor activities during peak heat hours. Wear lightweight, loose-fitting clothing and apply sunscreen regularly if venturing outdoors. Keep a close eye on vulnerable individuals such as the elderly, children, and pets, ensuring they stay cool and hydrated. Stay informed through local weather updates and heed any advisories issued by authorities. Let's prioritize safety and well-being during this intense heatwave."
                },
                card2: {
                    urlPhoto: "/forecast/snowy.svg",
                    message: "Slippery roads due to...",
                    warning: false,
                    time: "20:00 Today",
                    text: ""
                },
                card3: {
                    urlPhoto: "/forecast/stormy.svg",
                    message: "Thunderstorm warning!",
                    warning: true,
                    time: "15:00 Yesterday",
                    text: ""
                },
                card4: {
                    urlPhoto: "/forecast/sunny.svg",
                    message: "Dangerous heatwave alert!",
                    warning: true,
                    time: "11:00 Sat",
                    text: ""
                },
                card5: {
                    urlPhoto: "/forecast/sunny.svg",
                    message: "Perfect weather for out...",
                    warning: false,
                    time: "14:00 Fri",
                    text: ""
                }
            }
        }
    },
    methods: {
        normalizeGraph() {
            const maxValue = Math.max(...this.graph[this.activeDayIndex - 1]);
            const minValue = Math.min(...this.graph[this.activeDayIndex - 1]);
            return this.graph[this.activeDayIndex - 1].map(
                (price) => 35 + ((price - minValue) * 65) / (maxValue - minValue)
            );
        },
        setActiveDay(index){
            this.activeDayIndex = index;
        },
        setActiveCard(index){
            if(this.activeCardIndex == index) this.activeCardIndex = null;
            else this.activeCardIndex = index
        }
    }
}    
</script>

<style>
.weather-section{
    margin-top: 32px;
    display: flex;
    justify-content: space-between;
}
.forecast-part{
    width: 840px;
}
.current-day__info{
    display: flex;
    align-items: center;
    width: 812px;
    justify-content: space-between;

}
.weather-temperature{
    display: flex;
    align-items: center;
    
}
.current-day__icon{
    display: block;
    width: 91px;
    height: 91px;
}
.current-day__temp{
    margin-left: 32px;
    color: #95FAB3;
    font-size: 94px;
    font-weight: 300;
    align-items: center;
}
.temperature{
    color: #2B6769;
    font-weight: 900;

}
.current-date{
    font-size: 35px;
    font-weight: 700;
}
.current-place{
    text-align: center;
    color: #000;
    font-size: 22px;
    font-weight: 500;
}
.current-week-day{
    color: #2B6769;
}
.graphic-categories{
    margin-top: 20px;
    display: flex;
    gap: 75px;
    font-size: 22px;
    font-weight: 500;
    line-height: 136.7%; 
}
.graphic-category{
    position: relative;
    cursor: pointer;
}
.active-graphic-category::after{
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%; /* Ширина лінії рівна ширині блоку */
    border-bottom: 2px solid #95FAB3;; /* Змініть це на бажаний стиль і колір вашої лінії */
}
.graphic-impl{
    margin-top: 20px;
    padding-top: 30px;
    display: flex;
    gap: 7px;
    width: 840px;
    height: 277px;
    align-items: end;
}
.graphic-column{
    background: linear-gradient(180deg, #95FAB3 0%, #9AB7FF 100%);
    width: 47px;
    color: #8499CE;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.value{
    text-align: center;
    font-size: 17px;
    font-weight: 400;
    line-height: 162%;
}
.date{
    text-align: center;
    font-size: 13px;
    font-weight: 500;
    line-height: 162%;
}
.day-section{
    margin: 10px 0;
    display: flex;
    gap: 5px;
}
.day-card{
    width: 100px;
    height: 175px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    font-size: 22px;
    font-weight: 500;
}
.week-day{
    font-size: 22px;
}
.day-pic{
    width: 57px;
    height: 57px;
}
.min-temp{
    color: #8499CE;
}
.message-part{
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 20px;
}
.alert-block{
    display: flex;
    gap: 25px;
    background: #FFF;
    box-shadow: 0px 4px 7px 0px rgba(0, 0, 0, 0.25);
    width: 484px;
    height: 106px;
    padding: 25px 21px 26px 21px;
    justify-content: center;
    align-items: center;
}
.active-card{
    background-color: #EFEFEF;
}
.alert-icon{
    background-color: white;
    width: 53px;
    height: 53px;
}
.time-block{
    color: #9AB7FF;
    text-align: right;
    width: 90px;
    height: 50px;
}
.more-records-card{
    margin: 30px 0;
    color: #9AB7FF;
    font-size: 17px;
    font-weight: 500;
    text-align: center;
}
.blue-text{
    color: #9AB7FF;
}
.red-text{
    color: #FF0000;
}
.forecast-header{
    display: flex;
    align-items: center;
    gap: 36px;
}
.forecast-text{
    margin-top: 26px;
    font-size: 22px;
}

</style>