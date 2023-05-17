<script>
import axios from "axios";
import Chart from "chart.js/auto";

export default {
  data() {
    return {
      meditions: [],
      labelss: [],
      phValues: [],
      phChartData: [],
      phChartOptions: [],
      voltValues: [],
      voltChartData: [],
      currentValues: [],
      currentChartData: [],
    };
  },

  methods: {
    getData() {
      axios.get("http://127.0.0.1:8000/medition").then((response) => {
        this.meditions = response.data;
        let i = 10;
        const len = this.meditions.length;

        for (let number of Array(len)) {
          this.labelss.push(i);
          i = i + 10;
        }

        //Getting the values for the ph chart
        this.meditions.map((row) => this.phValues.push(row.Ph));

        this.phChartData = {
          labels: this.labelss,
          datasets: [
            {
              label: "PH",
              data: this.phValues,
            },
          ],
        };

        //Gettin the values for the voltage chart
        this.meditions.map((row) => this.voltValues.push(row.Voltage));

        this.voltChartData = {
          labels: this.labelss,
          datasets: [{ label: "Voltage", data: this.voltValues }],
        };

        //Getting the values for the current chart
        this.meditions.map((row) => this.currentValues.push(row.Current));

        this.currentChartData = {
          labels: this.labelss,
          datasets: [{ label: "Current", data: this.currentValues }],
        };

        //Setting the data for the ph Chart
        let ctx = document.getElementById("ph");

        const phChart = new Chart(ctx, {
          type: "line",
          data: this.phChartData,
        });

        //Setting the data for the voltage Chart
        ctx = document.getElementById("voltage");

        const voltChart = new Chart(ctx, {
          type: "line",
          data: this.voltChartData,
        });

        //Setting the data for the current Chart
        ctx = document.getElementById("current");

        const currentChart = new Chart(ctx, {
          type: "line",
          data: this.currentChartData,
        });

        //Calling all the chart settings
        phChart;
        voltChart;
        currentChart;
      });
    },
  },

  mounted: async function () {
    this.getData();
  },
};
</script>

<template>
  <div class="greetings">
    <h1 class="green">Charts</h1>
    <div style="width: 800px"><canvas id="ph"></canvas></div>
    <br />
    <br />
    <div style="width: 800px"><canvas id="voltage"></canvas></div>
    <br />
    <br />
    <div style="width: 800px"><canvas id="current"></canvas></div>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
