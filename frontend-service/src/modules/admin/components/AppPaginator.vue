<script setup lang="ts">
import AppPaginatorArrowPrev from './AppPaginatorArrowPrev.vue';
import AppPaginatorArrowNext from './AppPaginatorArrowNext.vue';
import { computed } from 'vue';

const props = defineProps<{ 
  lenght: number;
	currentPage: number;
}>();
const emit = defineEmits(['next', 'current']);

const items = computed(() => {
  const current = props.currentPage;
  const lenght = props.lenght;

  if(lenght == 1) {
    return [current];
  }

  if (lenght == 2) {
    return [current, current + 1];
  }

  if (lenght - current == lenght - 1) {
    return [current, current + 1, current + 2];
  }

  if (lenght - current > 0) {
    return [current - 1, current, current + 1];
  }
  
  if (lenght - current == 0) {
    return [current - 2, current -1, current]
  }

  return [];
});

const nextPage = () => {
  if (props.currentPage < props.lenght) {
    emit('current', props.currentPage + 1);
  }
};

const prevPage = () => {
  if(props.currentPage > 1) {
    emit('current', props.currentPage - 1);
  }
};
</script>

<template>
  <div class="paginator-container">
    <button
      class="paginator-button"
      @click="prevPage"
    >
      <AppPaginatorArrowPrev />
    </button>


    <template
      v-for="item in items"
      :key="item"
    >
      <button
        :class="[currentPage == item ? 'active' : 'paginator-button']"
        @click="$emit('current', item)"
      >
        {{ item }}
      </button>
    </template>


    <button
      class="paginator-button"
      @click="nextPage"
    >
      <AppPaginatorArrowNext />
    </button>
  </div>
</template>

<style scoped>
.paginator-container {
	display: flex;
	flex-direction: row;
	align-items: center;
}
.paginator-button {
    background-color: white;
	border-color: transparent;
	color: #8d8e9e;
	font-weight: 600;
	font-size: 14px;
	margin: 0 2px;
	width: 30px;
	height: 30px;
	border-radius: 6px;
	display: flex;
	flex-direction: row;
	align-items: center;
	justify-content: center;
	cursor: pointer;
}
.paginator-button:hover {
	background-color: #598bff;
	color: white;
}
.active {
  background-color: #598bff;
	border-color: transparent;
	color: white;
	font-weight: 600;
	font-size: 14px;
	margin: 0 2px;
	width: 30px;
	height: 30px;
	border-radius: 6px;
	display: flex;
	flex-direction: row;
	align-items: center;
	justify-content: center;
	cursor: pointer;
}
</style>