<script setup lang="ts">
defineProps<{ 
    title: string;
    fn: () => void;
}>();
</script>

<template>
  <button
    class="custom-button"
    @click="fn"
  >
    {{ title }}
  </button>
</template>

<style scoped>
.custom-button {
    background-color: #598bff;
    width: 100%;
    border-color: transparent;
    border-radius: 8px;
    padding: 3px 6px;
    color: white;
    font-size: 14px;
    font-weight: 700;
    cursor: pointer;
    animation: background 0.2s;
}
.custom-button:active {
    background-color: #517fe8;
}
</style>