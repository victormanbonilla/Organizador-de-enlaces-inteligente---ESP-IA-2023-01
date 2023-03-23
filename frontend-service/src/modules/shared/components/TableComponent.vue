<script setup lang="ts">
import { Consult } from '../interfaces/sharedTable';
import ShareIcon from './ShareIcon.vue';

const head = ['ID', 'CATEGORY', 'URL', 'CRETED AT'];

defineProps<{ 
  consults: Consult[]; 
  date: string; 
  index: number;
  code: string;
}>();
const shareTable = async (text: string) => {
    await navigator.clipboard.writeText(text);
};
</script>

<template>
  <div class="table-sub-container">
    <div class="info-table">
      <h1 style="color: #5c5b5b">
        Table {{ index }}
      </h1>

      <button
        class="icon-container"
        @click="shareTable(code)"
      >
        <ShareIcon />
      </button>
    </div>
    <table class="custom-table">
      <thead>
        <th />
        <th
          v-for="datum in head"
          :key="datum"
        >
          {{ datum }}
        </th>
      </thead>
      <tbody class="table-body">
        <tr
          v-for="(row, i) in consults"
          :key="i"
        >
          <td>
            <input
              id="example"
              type="checkbox"
              name="example"
            >
          </td>
          <td>{{ i }}</td>
          <td>{{ row.category }}</td>
          <td>{{ row.url }}</td>
          <td>{{ date }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.table-sub-container {
	background-color: transparent;
	width: 100%;
	height: 100%;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
}
.custom-table {
	text-align: center;
	width: 100%;
	height: 95%;
	border-collapse: collapse;
}
th {
	font-weight: 400;
	font-size: 15px !important;
	color: #4f4f4f;
	padding: 5px;
	border: 0.1px solid #e6e6e6;
	border-left: 0;
	border-right: 0;
	border-top: 0;
}
tbody tr {
	border: 0.1px solid #e6e6e6;
	border-left: 0px;
	border-right: 0px;
}
tbody tr:last-child {
	border: 0.1px solid #e6e6e6;
	border-left: 0px;
	border-right: 0px;
	border-bottom: 0;
}
tbody td {
	font-size: 15px !important;
	border: 0.1px solid #e6e6e6;
	padding: 9px 0;
	border-right: 0;
	border-left: 0;
	border-bottom: 0;
	color: #4f4f4f;
}
.info-table {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 5px 15px;
}
.info-table h1 {
  font-size: 22px !important;
}
.icon-container {
  border-color: transparent;
  border-radius: 8px;
  padding: 2px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  background-color: #598bff;
  cursor: pointer;
}
</style>
