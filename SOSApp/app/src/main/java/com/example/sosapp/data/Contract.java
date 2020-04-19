package com.example.sosapp.data;

import android.provider.BaseColumns;

public final class Contract {

    private Contract() {
    }

    public static final class Entry implements BaseColumns {

        public final static String TABLE_NAME = "SOS_Database";
        public final static String _ID = BaseColumns._ID;
        public final static String NAME = "Name";
        public final static String NUMBER = "Number";
    }
}
