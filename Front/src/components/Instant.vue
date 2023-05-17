<script>
import axios from "axios";
export default {
  data() {
    return {
      meditions: [],
      phValue: [],
      voltValue: [],
      currentValue: [],
    };
  },

  methods: {
    getInstant() {
      axios.get("http://127.0.0.1:8000/medition").then((response) => {
        this.meditions = response.data;
        const len = this.meditions.length;
        let c = 0;
        for (let number of Array(len)) {
          c = c + 1;
        }

        //Fill the vetor for each value
        this.meditions.map((row) => this.phValue.push(row.Ph));
        this.meditions.map((row) => this.voltValue.push(row.Voltage));
        this.meditions.map((row) => this.currentValue.push(row.Current));

        //Print the value of each element
        const pushInfoPh = document.getElementById("ph");
        pushInfoPh.innerHTML = this.phValue[c-1];

        const pushInfoVolt = document.getElementById("volt");
        pushInfoVolt.innerHTML = this.voltValue[c-1];

        const pushInfoCurrent = document.getElementById("current");
        pushInfoCurrent.innerHTML = this.currentValue[c-1];
      });
    },

    dataClick() {
      axios.post("http://127.0.0.1:8000/medition").then((response) =>{
        alert(done)
      })
    }
  },

  mounted: function () {
    this.getInstant();
  },
};
</script>

<template>
  <div class="greetings">
    <h1 class="green">Instantaneous</h1>
    <table class="table table-striped table-dark">
      <thead>
        <tr>
          <th scope="col">Ph</th>
          <th scope="col">Voltage</th>
          <th scope="col">Current</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td id="ph">1</td>
          <td id="volt">1</td>
          <td id="current">1</td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class="d-flex justify-content-center">
    <button class="btn btn-dark" @click="dataClick()">get data</button>
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
