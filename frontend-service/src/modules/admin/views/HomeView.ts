import { inject, onMounted, ref, defineComponent, markRaw, computed } from 'vue';
import { ElMessage, ElDialog } from 'element-plus';
import { useForm } from 'vee-validate';

import TableComponent from '../components/TableComponent.vue';
import AppInputArray from '../components/AppInputArray.vue';
import ShareModal from '../components/ShareModal.vue';
import AppSpinner from '../components/AppSpinner.vue';
import AppModal from '../components/AppModal.vue';

import { useConsults } from '../composables/useConsults';
import { keyFormState } from '../utils/formKey';
import { Table } from '../interfaces/consult';
import { object, string, array } from 'yup';

interface ConsultForm {
  consults: Array<{ url: string; id: number }>;
}

export default defineComponent({
  name: 'HomeView',
  components: {
    TableComponent,
    AppInputArray,
    ShareModal,
    AppSpinner,
    AppModal,
    ElDialog,
  },
  setup: () => {
    const urlRegex = /^(https:\/\/)(www\.)?[a-z0-9]+(\.[a-z]{2,}){1,3}(#?\/?[a-zA-Z0-9#]+)*\/?(\?[a-zA-Z0-9-_]+=[a-zA-Z0-9-%]+&?)?$/;
    const schema = markRaw(
      object({
        consults: array().of(
          object({
            url: string()
              .matches(urlRegex, 'Enter a valid url')
              .required('Please enter a value'),
          })
        ),
      })
    );

    const { getConsults, saveConsults, deleteTable } = useConsults();
    const { handleSubmit, resetForm, meta } = useForm<ConsultForm>({
      initialValues: {
        consults: [{ url: '', id: 0 }],
      },
      validationSchema: schema,
    });

    const data = ref<Table[]>();
    const [formState, setFormState] = inject(keyFormState)!;
    const spinnerState = ref(false);
    const validForm = computed(() => !meta.value.valid);
    const activeModalShare = ref(false);
    const sharedText = ref("");

    const success = () => {
      ElMessage({
        showClose: true,
        message: 'Success',
        type: 'success',
      });
    };

    const getData = async () => {
      data.value = await getConsults();
    };

    const onSubmit = handleSubmit(async ({ consults }, { resetForm }) => {
      const data = consults.map((consult) => consult.url);
      const resp = await saveConsults(data, spinnerState);
      resetForm();
      if (resp) {
        success();
        setFormState();
        await getData();
      }
    });

    const onClose = () => {
      setFormState();
      resetForm({
        values: {
          consults: [{ url: '', id: 0 }],
        },
      });
    };

    const onDelete = async (code: string) => {
      const resp = await deleteTable(code);
      if (resp) {
        success();
        getData();
      }
    };

    const shareTable = async () => {
      await navigator.clipboard.writeText(
        `https://demo.vbonilla.com/#/public/${sharedText.value}/`
      );
      activeModalShare.value = false;
      success();
    };

    onMounted(async () => {
      await getData();
    });

    return {
      // Methods
      setFormState,
      deleteTable,
      shareTable,
      onSubmit,
      onDelete,
      onClose,

      // Properties
      activeModalShare,
      spinnerState,
      sharedText,
      formState,
      validForm,
      data,
      meta,

      // Componentes
      TableComponent,
      AppInputArray,
      AppSpinner,
      AppModal,
      ElDialog,
    };
  },
});
