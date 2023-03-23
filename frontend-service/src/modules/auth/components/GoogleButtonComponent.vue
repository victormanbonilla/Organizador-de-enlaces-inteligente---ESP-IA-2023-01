<script setup lang="ts">
import GoogleIcon from './GoogleIcon.vue';

const href = () => {
	console.log("Funcionma");
};
</script>

<template>
  <button
    class="Google-button"
    type="button"
    disabled
    @click="href()"
  >
    <GoogleIcon />
    <span>Continue with google</span>
  </button>
</template>

<style scoped>
.Google-button {
	display: flex;
	align-items: center;
	justify-content: center;
	width: 94%;
	height: 12%;
	border: none;
	background: #f75771;
	border-radius: 10px;
	cursor: pointer;
}
.Google-button:focus {
	outline: none;
}
button span {
	margin-left: 10px;
	color: white;
	font-size: 12px;
}
.Google-button:enabled:active {
	background-color: #ed536c;
}
.Google-button:disabled {
	background-color: #d4485f;
	cursor: default;
}
</style>
