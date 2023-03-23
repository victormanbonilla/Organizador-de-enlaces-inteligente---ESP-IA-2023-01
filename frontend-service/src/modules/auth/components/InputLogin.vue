<script setup lang="ts">
import { Field, ErrorMessage } from 'vee-validate';

defineProps<{
	id: string;
	label: string;
	name: string;
	type: string;
	placeholder: string;
}>();

defineEmits<{
	// eslint-disable-next-line no-unused-vars
	(event: 'update:modelValue', payload: string): void;
}>();
</script>

<template>
  <div class="formcontrol-container">
    <label
      class="login-label"
      :for="id"
    >{{ label }}</label>
    <Field
      :id="id"
      :name="name"
      :type="type"
      class="login-input"
      :placeholder="placeholder"
    />
    <ErrorMessage
      :name="name"
      class="custom-error-message"
    />
  </div>
</template>

<style scoped>
.custom-error-message {
	font-size: 12px;
	padding-left: 10px;
	color: red;
	font-weight: 500;
}
.formcontrol-container {
	width: 95%;
	height: 30%;
	display: flex;
	flex-direction: column;
	align-items: flex-start;
	padding-top: 10px;
}
.login-label {
	font-size: 13px;
	font-weight: 600;
	text-align: start;
	padding-left: 10px;
}
.login-input {
	background-color: #fafafb;
	border-radius: 15px;
	height: 60%;
	width: 100%;
	border: 0.1px solid #f1f1f5;
	padding-left: 10px;
	color: 92929D;
}
.login-input::placeholder {
	font-size: 13.3px;
}
.login-input:focus{
	outline: none;
}
</style>
