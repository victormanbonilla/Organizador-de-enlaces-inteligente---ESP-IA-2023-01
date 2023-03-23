<script setup lang="ts">
defineProps<{ active: boolean}>();
</script>
<template>
  <div
    v-if="active"
    class="spinner-container"
  >
    <div class="spinner-sub-container">
      <div class="spinner" />
    </div>
  </div>
</template>

<style scoped>
.spinner {
  top: 0;
  left: 0;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: radial-gradient(farthest-side, #9167cc 94%, #0000) top/9px 9px
      no-repeat,
    conic-gradient(#0000 30%, #9167cc);
  mask: radial-gradient(farthest-side, #0000 calc(100% - 9px), #000 0);
  animation: spinner-c7wet2 1s infinite linear;
}

@keyframes spinner-c7wet2 {
  100% {
    transform: rotate(1turn);
  }
}

.spinner-container {
  position: relative;
  width: 0;
  height: 0;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.spinner-sub-container {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 3;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  background-color: rgba(0, 0, 0, 0.2);
}
</style>
