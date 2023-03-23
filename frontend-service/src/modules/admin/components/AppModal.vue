<script setup lang="ts">
defineProps<{ active: boolean }>();
</script>

<template>
  <div
    v-if="active"
    class="modal-container"
  >
    <div class="modal-sub-container">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.modal-container {
  position: fixed;
  background-color: rgba(0, 0, 0, 0.75);
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.modal-container:target {
  opacity: 1;
}
.modal-sub-container {
  min-width: 416.7px;
  min-height: 486.5px;
  background-color: white;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
