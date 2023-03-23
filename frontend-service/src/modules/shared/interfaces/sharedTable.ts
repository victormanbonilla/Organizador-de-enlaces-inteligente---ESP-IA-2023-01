export interface getSharedTable {
    data:    SharedTable;
    code:    number;
    message: string;
}

export interface SharedTable  {
    code:       string;
    data:       Consult[];
    created_at: string;
}

export interface Consult {
    category: string;
    url:      string;
}
