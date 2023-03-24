<script setup lang="ts">
import { Field, useFieldArray, ErrorMessage } from 'vee-validate';
import { ref } from 'vue';
import AddFormIcon from './AddFormIcon.vue';
import TrashIcon from './TrashIcon.vue';
import UrlIcon from './UrlIcon.vue';

const props = defineProps<{
  placeholder: string;
  arrName: string;
  title: string;
  id: string;
}>();
const { remove, push, fields } = useFieldArray<{ url: string; id: number }>(
  props.arrName
);
const arrayState = ref(fields.value.length + 1);
</script>

<template>
  <div class="app-input-container">
    <div
      v-for="(_, index) in fields"
      :key="`item${index}`"
      class="form-controls-container"
    >
      <label :for="id">{{ title }}</label>
      <div class="form-control-container">
        <div class="input-container">
          <UrlIcon class="search-icon" />
          <Field
            :id="id"
            type="search"
            class="custom-input"
            :name="`${arrName}[${index}].url`"
            :placeholder="placeholder"
          />
        </div>
        <button
          class="btn-delete"
          type="button"
          @click="remove(index)"
        >
          <TrashIcon />
        </button>
      </div>
      <div class="error-message-container">
        <ErrorMessage
          :name="`${arrName}[${index}].url`"
          class="custom-error-message"
        />
      </div>
    </div>
    <div class="btn-add-container">
      <button
        class="btn-add"
        type="button"
        @click="
          push({ url: '', id: arrayState });
          arrayState++;
        "
      >
        <AddFormIcon />
      </button>
    </div>
  </div>
</template>

<style scoped>
.error-message-container {
  width: 100%;
  height: fit-content;
}
.custom-error-message {
  font-size: 12px;
  padding-left: 10px;
  color: red;
  font-weight: 500;
}
.app-input-container {
  width: 100%;
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
  width: 93%;
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
  color: #8d8e9e;
}
.form-controls-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: space-between;
  width: 100%;
  padding-bottom: 10px;
}
.btn-delete {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  border: 2px solid #9167cc;
  width: 26px;
  height: 26px;
  border-radius: 4px;
  color: #9167cc;
  background-color: white;
  cursor: pointer;
  transition: background 0.1s;
  float: right;
}
.btn-delete:hover {
  background-color: #9167cc;
  color: white;
}
.btn-add {
  float: right;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  border: 2px solid #598bff;
  width: 26px;
  height: 26px;
  border-radius: 4px;
  background-color: white;
  color: #598bff;
  cursor: pointer;
  transition: background 0.1s;
}
.btn-add:hover {
  background-color: #598bff;
  color: white;
}
.btn-add-container {
  width: 100%;
  height: fit-content;
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: flex-end;
  padding-bottom: 5px;
}
.form-control-container {
  width: 100%;
  height: fit-content;
  display: flex;
  flex-direction: row;
  align-items: center;
}
</style>
