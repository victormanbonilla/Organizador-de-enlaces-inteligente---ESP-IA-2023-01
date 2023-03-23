

<template>
  <div class="modal-container">
    <slot />
  </div>
</template>

<style scoped>
.modal-container {
	width: 355.15px;
	height: 384px;
	background-color: #ffffff;
	border-radius: 20px;
	text-align: center;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
}
</style>
