 for c in {1..89};do echo '& (df_tmp[self._columns["Low"]] < df_tmp[self._columns["Low"]].shift('$c'))';done;for c in {-1..-89};do echo '& (df_tmp[self._columns["Low"]] < df_tmp[self._columns["Low"]].shift('$c'))';done

 for c in {1..89};do echo '& (df_tmp[self._columns["High"]] > df_tmp[self._columns["High"]].shift('$c'))';done;for c in {-1..-89};do echo '& (df_tmp[self._columns["High"]] > df_tmp[self._columns["High"]].shift('$c'))';done
