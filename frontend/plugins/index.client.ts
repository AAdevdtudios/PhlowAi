import {defineNuxtPlugin} from '#app'
import Donut from 'vue-css-donut-chart';

import * as ChartJs from 'chart.js'
const {Chart, registerables }= ChartJs;

export default defineNuxtPlugin(nuxtApp =>{
    nuxtApp.vueApp.use(Donut)
    Chart.register(...registerables)
})