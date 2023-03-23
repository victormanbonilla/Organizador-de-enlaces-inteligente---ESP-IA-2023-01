<script setup lang="ts">import { computed } from 'vue';

const props = defineProps<{ 
    items: Array<{ 
        id: number; 
        label: string
    }>; 
    id: string; 
    label: string;
    lbPosition: 'left' | 'top';
}>();
defineEmits(['input']);

function cleanInput(e: Event) {
    return (e.target as HTMLInputElement).value;
}

const labelPosition = computed(() => {
    return props.lbPosition == 'top' 
        ? 'custom-input-filter-top' 
        : 'custom-input-filter-left'
})
</script>

<template>
  <div :class="[labelPosition]">
    <label
      :for="id"
      class="custom-label"
    >{{ label }}</label>
    <select
      :id="id"
      :name="id"
      class="custom-select"
      @input="val => $emit('input', cleanInput(val))"
    >
      <option
        v-for="item in items"
        v-once
        :key="item.id"
        :value="item.id"
      >
        {{ item.label }}
      </option>
    </select>
  </div>
</template>

<style scoped>
.custom-input-filter-top {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.custom-input-filter-left {
    display: flex;
    flex-direction: row;
    align-items: center;
}
.custom-select {
    border-color: transparent;
    background-color: #f2f2f2;
    border-radius: 6px;
    width: 100%;
    padding: 4px 0 4px 13px;
    color: #c2c2cb;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
}
.custom-label {
    font-size: 13px;
    font-weight: 600;
    margin: 0 15px 5px 5px;
}
</style>