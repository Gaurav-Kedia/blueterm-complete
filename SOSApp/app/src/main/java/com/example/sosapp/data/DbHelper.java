package com.example.sosapp.data;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import com.example.sosapp.data.Contract.Entry;

import static com.example.sosapp.data.Contract.Entry.TABLE_NAME;

public class DbHelper extends SQLiteOpenHelper {

    private static final String DATABASE_NAME = "SOS_DATABASE.db";
    private static final int DATABASE_VERSION = 1;

    public DbHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {

        String SQL_CREATE_TABLE =  "CREATE TABLE " + TABLE_NAME + " ("
                + Entry._ID + " INTEGER PRIMARY KEY AUTOINCREMENT, "
                + Entry.NAME + " TEXT NOT NULL, "
                + Entry.NUMBER + " TEXT NOT NULL);";

        // Execute the SQL statement
        db.execSQL(SQL_CREATE_TABLE);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS "+TABLE_NAME);
        onCreate(db);
    }
}
