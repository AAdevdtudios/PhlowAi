<template>
    <div class="items">
        <h4>{{name}}</h4>
        <div class="item-flex">
            <div class="right">
                <!-- <RadarChart :chartData="radarChat"/> -->
                <DoughnutChart :chartData = "doughChartData" :width="200" :height="200" />
                <div>
                    <div class="activities">
                        <div class="box bg-pri/90">
                        </div>
                        <h5>Activities</h5>
                        <span>100</span>
                    </div>
                    <div class="activities">
                        <div class="box bg-slate-900">
                        </div>
                        <h5>Activities</h5>
                        <span>100</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
import { DoughnutChart, RadarChart } from "vue-chart-3";
import {Chart, registerables} from 'chart.js'
Chart.register(...registerables)

interface Props{
    name: string
}
const value = defineProps<Props>();

let radarChat ={
    labels: [
      "Eating",
      "Drinking",
      "Sleeping",
      "Designing",
      "Coding",
      "Cycling",
      "Running",
    ],
    datasets: [
      {
        label: "My First Dataset",
        data: [65, 59, 90, 81, 56, 55, 40],
        fill: true,
        backgroundColor: "rgba(133, 105, 241, 0.2)",
        borderColor: "rgb(133, 105, 241)",
        pointBackgroundColor: "rgb(133, 105, 241)",
        pointBorderColor: "#fff",
        pointHoverBackgroundColor: "#fff",
        pointHoverBorderColor: "rgb(133, 105, 241)",
      },
      {
        label: "My Second Dataset",
        data: [28, 48, 40, 19, 96, 27, 100],
        fill: true,
        backgroundColor: "rgba(54, 162, 235, 0.2)",
        borderColor: "rgb(54, 162, 235)",
        pointBackgroundColor: "rgb(54, 162, 235)",
        pointBorderColor: "#fff",
        pointHoverBackgroundColor: "#fff",
        pointHoverBorderColor: "rgb(54, 162, 235)",
      },
    ]
}

let doughChartData = {
    datasets: [
        {
            label: value.name,
            data: [72, 131,],
            backgroundColor: [
                'rgb(240 216 8 / 0.9)',
                'rgb(15 23 42 /1)'
            ],
            borderColor: 'rgba(100, 155, 0, 1)',
            borderWidth: 0
        }
    ]
}
</script>