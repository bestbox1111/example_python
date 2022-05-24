from openpyxl import load_workbook, Workbook

# wb= Workbook()
# ws=wb.active
#전체 컨셉은 셀병합
# ws.merge_cells("B2:D2")
# ws["B2"].value="merged cell park"

# wb.save("sample_cell_merge.xlsx")


##

#전체 컨셉은 위에서 병합된 셀을 해제시키기
wb=load_workbook("sample_cell_merge.xlsx")
ws=wb.active

ws.unmerge_cells("B2:D2")
wb.save("sample_cell_unmerge.xlsx")