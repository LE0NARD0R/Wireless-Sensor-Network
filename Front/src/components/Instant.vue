<script>
import axios from "axios";
export default {
  data() {
    return {
      meditions: [],
      phValue: [],
      voltValue: [],
      currentValue: [],
      node: [],
      instant:[],
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
        this.meditions.map((row) => this.node.push(row.Node));
        this.meditions.map((row) => this.phValue.push(row.Ph));
        this.meditions.map((row) => this.voltValue.push(row.Voltage));
        this.meditions.map((row) => this.currentValue.push(row.Current));
        this.meditions.map((row) => this.instant.push(row));
        console.log(this.node);
        console.log('instant:', this.instant);


        //Print the value of each element
        
        const pushInfoNode = document.getElementById("node");
        pushInfoNode.innerHTML = this.node[c-1];

        const pushInfoPh = document.getElementById("ph");
        pushInfoPh.innerHTML = this.phValue[c-1];

        const pushInfoVolt = document.getElementById("volt");
        pushInfoVolt.innerHTML = this.voltValue[c-1];

        const pushInfoCurrent = document.getElementById("current");
        pushInfoCurrent.innerHTML = this.currentValue[c-1];

        const pushInfoNode1 = document.getElementById("node1");
        pushInfoNode1.innerHTML = this.node[c-2];

        const pushInfoPh1 = document.getElementById("ph1");
        pushInfoPh1.innerHTML = this.phValue[c-2];

        const pushInfoVolt1 = document.getElementById("volt1");
        pushInfoVolt1.innerHTML = this.voltValue[c-2];

        const pushInfoCurrent1 = document.getElementById("current1");
        pushInfoCurrent1.innerHTML = this.currentValue[c-2];
      });
    },

    dataClick() {
      axios.post("http://127.0.0.1:8000/medition").then((response) =>{
        console.log('done');
      })
    }
  },

  mounted: function () {
    this.dataClick();
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
          <th scope="col">Node</th>
          <th scope="col">Ph</th>
          <th scope="col">Voltage</th>
          <th scope="col">Current</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td id="node">1</td>
          <td id="ph">1</td>
          <td id="volt">1</td>
          <td id="current">1</td>
        </tr>
        <tr>
          <td id="node1">2</td>
          <td id="ph1">1</td>
          <td id="volt1">1</td>
          <td id="current1">1</td>
        </tr>
      </tbody>
    </table>
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
