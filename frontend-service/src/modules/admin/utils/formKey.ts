import { InjectionKey, Ref } from "vue";

const keyFormState = Symbol () as InjectionKey<[Ref<boolean>, () => boolean]>;

export { keyFormState }; 