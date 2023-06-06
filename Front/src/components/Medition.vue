<script>
import axios from "axios";
export default {
  data() {
    return {
      meditions: [],
    };
  },

  methods: {
    refreshData() {
      axios.get("http://127.0.0.1:8000/medition").then((response) => {
        this.meditions = response.data;
      });
    },
  },

  mounted: function () {
    this.refreshData();
  },
};
</script>

<template>
  <div class="greetings">
    <h1 class="green">Meditions</h1>
    <table class="table table-striped table-dark">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Node</th>
          <th scope="col">Ph</th>
          <th scope="col">Voltage</th>
          <th scope="col">Current</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="med, i in meditions" :key="med.MeditionsId" >
          <td>{{ (i+1) }}</td>
          <td>{{ med.Node }}</td>
          <td>{{ med.Ph }}</td>
          <td>{{ med.Voltage }}</td>
          <td>{{ med.Current }}</td>
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
