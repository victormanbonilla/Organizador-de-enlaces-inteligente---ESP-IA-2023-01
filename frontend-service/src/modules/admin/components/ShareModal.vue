<script setup lang="ts">
import AppModal from './AppModal.vue';

defineProps<{ active: boolean; link: string }>();
defineEmits(['copy']);
</script>

<template>
  <AppModal :active="active">
    <h1>Hola mundo</h1>
    <div>
      <span>{{ link || '' }}</span>
      <button @click="$emit('copy')">
        Copy
      </button>
    </div>
  </AppModal>
</template>

<style scoped></style>
