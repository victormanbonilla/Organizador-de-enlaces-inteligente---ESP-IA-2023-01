<script setup lang="ts">
// import AppInputSearchIcon from './AppInputSearchIcon.vue';

defineProps<{ 
	title: string; 
	placeholder: string; 
	id: string 
}>();
defineEmits(['input']);
</script>

<template>
  <div class="app-input-container">
    <label :for="id">{{ title }}</label>
    <div class="input-container">
      <!-- <AppInputSearchIcon class="search-icon" /> -->
      <input
        :id="id"
        type="search"
        class="custom-input"
        :name="id"
        :placeholder="placeholder"
      >
    </div>
  </div>
</template>

<style scoped>
.app-input-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.app-input-container label {
    font-size: 13px;
    font-weight: 600;
		margin: 0 0 5px 5px;
}
.input-container {
	position: relative;
	display: flex;
	flex-direction: row;
	align-items: center;
	width: 100%;
}
.custom-input {
	border-color: transparent;
	border-radius: 8px;
	padding: 3px 0 3px 30px;
	width: 100%;
	background-color: #f2f2f2;
}
.custom-input::placeholder {
	color: #8d8e9e;
	font-size: 13px;
	font-weight: 600;
}
.custom-input:focus {
	outline: none;
	transition: 0.5s; 
	opacity: 1;
}
.search-icon {
	position: absolute;
	left: 5px;
}
</style>
