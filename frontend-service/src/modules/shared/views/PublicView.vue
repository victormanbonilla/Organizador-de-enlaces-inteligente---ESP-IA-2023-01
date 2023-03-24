<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { http } from '../../../environments/environment.prod';
import { useRoute } from 'vue-router';
import TableComponent from '../components/TableComponent.vue';
import { getSharedTable, SharedTable } from '../interfaces/sharedTable';

const { params } = useRoute();
const table = ref<SharedTable>();

onMounted(async () => {
  const id = params.id;
  const { data } = await http.get<getSharedTable>(`https://app.vbonilla.com/api/lists/share/${id}`);
  table.value = data.data;
});
</script>

<template>
  <div
    v-if="table"
    class="public-view-container"
  >
    <div class="table-container">
      <TableComponent
        :consults="table.data"
        :date="table.created_at"
        :index="0"
        :code="table.code"
      />
    </div>
  </div>
</template>

<style scoped>
.public-view-container {
  background-color: #e6e8ea;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  height: 100%;
  width: 100%;
}
.table-container {
  background-color: white;
  width: 60%;
  height: fit-content;
  padding: 15px;
  border-radius: 12px;
}
</style>
