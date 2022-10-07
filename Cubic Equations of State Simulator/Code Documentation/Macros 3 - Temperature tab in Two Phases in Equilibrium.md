# "Temperature" tab in "Two Phases in Equilibrium.xlsm" file

This spreadsheet allows performing calculations with the simulator results or experimental data of the thermodynamic properties in saturated liquid–vapor mixture based on temperature.

## 1. Spreadsheet Design

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/macros3-1.jpg" width="1038" height="433">

*Figure 1. Spreadsheet Design of "Temperature" tab in "Two Phases in Equilibrium.xlsm".*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/macros3-2.jpg" width="948" height="474">

*Figure 2. Controls properties.*

## 2. Excel Macro Code

```vbscript
Private Sub CLEAN_Click()
    Dim row As Integer ' Helper to pass rows
    FUGACITY_TEST.Enabled = True
    FUGACITY_TEST.Value = True
    EXPERIMENTAL_DATA.Enabled = True
    COMPUTE.Enabled = True
    CLEAN.Enabled = False
    With Workbooks("Two Phases in Equilibrium.xlsm").Worksheets("Temperature")
        .Range("B3:B9").Value = ""
        .Range("L14").Value = ""
        .Range("P18").Value = ""
        .Range("O18").Value = "x"
        .Range("L14").Select
        With Selection.Validation
            .Delete
            .Add Type:=xlValidateCustom, AlertStyle:=xlValidAlertStop, Operator:= _
            xlBetween, Formula1:="=ISBLANK(L14)"
            .IgnoreBlank = True
            .InCellDropdown = True
            .InputTitle = ""
            .ErrorTitle = ""
            .InputMessage = ""
            .ErrorMessage = ""
            .ShowInput = True
            .ShowError = True
        End With
        .Range("P18").Select
        With Selection.Validation
            .Delete
            .Add Type:=xlValidateCustom, AlertStyle:=xlValidAlertStop, Operator:= _
            xlBetween, Formula1:="=ISBLANK(P18)"
            .IgnoreBlank = True
            .InCellDropdown = True
            .InputTitle = ""
            .ErrorTitle = ""
            .InputMessage = ""
            .ErrorMessage = ""
            .ShowInput = True
            .ShowError = True
        End With
        row = 0
        While .Cells(12 + row, 1).Value <> ""
            .Range(Cells(12 + row, 1), Cells(12 + row, 10)).Value = ""
            .Range(Cells(12 + row, 1), Cells(12 + row, 10)).Select
            Selection.Borders(xlDiagonalDown).LineStyle = xlNone
            Selection.Borders(xlDiagonalUp).LineStyle = xlNone
            Selection.Borders(xlEdgeLeft).LineStyle = xlNone
            Selection.Borders(xlEdgeBottom).LineStyle = xlNone
            Selection.Borders(xlEdgeRight).LineStyle = xlNone
            Selection.Borders(xlInsideVertical).LineStyle = xlNone
            Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
            row = row + 1
        Wend
        .Range("L13").Formula2R1C1 = "=IF(R[1]C[0]="""",""-"",MAX(IF(R[-1]C[-11]:R[-1]C[-11]<=R[1]C[0],R[-1]C[-11]:R[-1]C[-11])))"
        .Range("M13").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-1]C[-12]:R[-1]C[-3],2,FALSE),""-"")"
        .Range("N13").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-1]C[-13]:R[-1]C[-4],5,FALSE),""-"")"
        .Range("O13").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-1]C[-14]:R[-1]C[-5],6,FALSE),""-"")"
        .Range("P13").Formula2R1C1 = "=IF(R[0]C[-4]<>""-"",VLOOKUP(R[0]C[-4],R[-1]C[-15]:R[-1]C[-6],7,FALSE),""-"")"
        .Range("Q13").Formula2R1C1 = "=IF(R[0]C[-5]<>""-"",VLOOKUP(R[0]C[-5],R[-1]C[-16]:R[-1]C[-7],8,FALSE),""-"")"
        .Range("R13").Formula2R1C1 = "=IF(R[0]C[-6]<>""-"",VLOOKUP(R[0]C[-6],R[-1]C[-17]:R[-1]C[-8],9,FALSE),""-"")"
        .Range("S13").Formula2R1C1 = "=IF(R[0]C[-7]<>""-"",VLOOKUP(R[0]C[-7],R[-1]C[-18]:R[-1]C[-9],10,FALSE),""-"")"
        .Range("L15").Formula2R1C1 = "=IF(R[-1]C[0]="""",""-"",MIN(IF(R[-3]C[-11]:R[-3]C[-11]>=R[-1]C[0],R[-3]C[-11]:R[-3]C[-11])))"
        .Range("M15").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-3]C[-12]:R[-3]C[-3],2,FALSE),""-"")"
        .Range("N15").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-3]C[-13]:R[-3]C[-4],5,FALSE),""-"")"
        .Range("O15").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-3]C[-14]:R[-3]C[-5],6,FALSE),""-"")"
        .Range("P15").Formula2R1C1 = "=IF(R[0]C[-4]<>""-"",VLOOKUP(R[0]C[-4],R[-3]C[-15]:R[-3]C[-6],7,FALSE),""-"")"
        .Range("Q15").Formula2R1C1 = "=IF(R[0]C[-5]<>""-"",VLOOKUP(R[0]C[-5],R[-3]C[-16]:R[-3]C[-7],8,FALSE),""-"")"
        .Range("R15").Formula2R1C1 = "=IF(R[0]C[-6]<>""-"",VLOOKUP(R[0]C[-6],R[-3]C[-17]:R[-3]C[-8],9,FALSE),""-"")"
        .Range("S15").Formula2R1C1 = "=IF(R[0]C[-7]<>""-"",VLOOKUP(R[0]C[-7],R[-3]C[-18]:R[-3]C[-9],10,FALSE),""-"")"
        .Columns("A:S").EntireColumn.AutoFit
        .Columns("B:D").ColumnWidth = 9.71
        .Columns("K:M").ColumnWidth = 9.71
        .Range("A3").Select
    End With
End Sub

Private Sub COMPUTE_Click()
    Dim row As Integer ' Helper to pass rows
    Dim row_data As Integer ' Number of rows of data
    If FUGACITY_TEST.Value = True Then
        ' Check if it is possible to export results
        If Workbooks("Two Phases in Equilibrium.xlsm").Worksheets("Temperature").Range("A12") <> "" Then
            MsgBox "Information is found in the data area.", vbExclamation
            Exit Sub
        End If
        If Workbooks("Two-Phase Envelope on a PV Diagram.xlsm").Worksheets("PV Diagram").Range("B1") <> Workbooks("Two-Phase Envelope on a PH Diagram.xlsm").Worksheets("PH Diagram").Range("B1") Or Workbooks("Two-Phase Envelope on a PV Diagram.xlsm").Worksheets("PV Diagram").Range("B1") <> Workbooks("Two-Phase Envelope on a PS Diagram.xlsm").Worksheets("PS Diagram").Range("B1") Or Workbooks("Two-Phase Envelope on a PH Diagram.xlsm").Worksheets("PH Diagram").Range("B1") <> Workbooks("Two-Phase Envelope on a PS Diagram.xlsm").Worksheets("PS Diagram").Range("B1") Then
            MsgBox "The value of COMPOUND does not match between spreadsheets.", vbExclamation
            Exit Sub
        End If
        If Workbooks("Two-Phase Envelope on a PV Diagram.xlsm").Worksheets("PV Diagram").Range("B2") <> Workbooks("Two-Phase Envelope on a PH Diagram.xlsm").Worksheets("PH Diagram").Range("B2") Or Workbooks("Two-Phase Envelope on a PV Diagram.xlsm").Worksheets("PV Diagram").Range("B2") <> Workbooks("Two-Phase Envelope on a PS Diagram.xlsm").Worksheets("PS Diagram").Range("B2") Or Workbooks("Two-Phase Envelope on a PH Diagram.xlsm").Worksheets("PH Diagram").Range("B2") <> Workbooks("Two-Phase Envelope on a PS Diagram.xlsm").Worksheets("PS Diagram").Range("B2") Then
            MsgBox "The value of CUBIC EQUATION OF STATE does not match between spreadsheets.", vbExclamation
            Exit Sub
        End If
        If Workbooks("Two-Phase Envelope on a PH Diagram.xlsm").Worksheets("PH Diagram").Range("B3") <> Workbooks("Two-Phase Envelope on a PS Diagram.xlsm").Worksheets("PS Diagram").Range("B3") Then
            MsgBox "The value of REFERENCE STATE does not match between spreadsheets.", vbExclamation
            Exit Sub
        End If
        If Workbooks("Two-Phase Envelope on a PH Diagram.xlsm").Worksheets("PH Diagram").Range("B4") <> Workbooks("Two-Phase Envelope on a PS Diagram.xlsm").Worksheets("PS Diagram").Range("B4") Then
            MsgBox "The value of REFERENCE TEMPERATURE [K] does not match between spreadsheets.", vbExclamation
            Exit Sub
        End If
        If Workbooks("Two-Phase Envelope on a PH Diagram.xlsm").Worksheets("PH Diagram").Range("B5") <> Workbooks("Two-Phase Envelope on a PS Diagram.xlsm").Worksheets("PS Diagram").Range("B5") Then
            MsgBox "The value of REFERENCE PRESSURE [BAR] does not match between spreadsheets.", vbExclamation
            Exit Sub
        End If
        With Workbooks("Two Phases in Equilibrium.xlsm").Worksheets("Temperature")
            ' Export results
            .Range("B3:B8").Value = Workbooks("Two-Phase Envelope on a PH Diagram.xlsm").Worksheets("PH Diagram").Range("B1:B6").Value
            .Range("B9").Value = Workbooks("Two-Phase Envelope on a PS Diagram.xlsm").Worksheets("PS Diagram").Range("B6").Value
            row = 0
            While Workbooks("Two-Phase Envelope on a PV Diagram.xlsm").Worksheets("PV Diagram").Cells(6 + 3 * row, 1).Value <> ""
                .Cells(12 + row, 1).Value = Workbooks("Two-Phase Envelope on a PV Diagram.xlsm").Worksheets("PV Diagram").Cells(6 + 3 * row, 2).Value
                .Cells(12 + row, 2).Value = Workbooks("Two-Phase Envelope on a PV Diagram.xlsm").Worksheets("PV Diagram").Cells(6 + 3 * row, 3).Value
                .Cells(12 + row, 3).Value = Workbooks("Two-Phase Envelope on a PV Diagram.xlsm").Worksheets("PV Diagram").Cells(6 + 3 * row, 4).Value
                .Cells(12 + row, 4).Value = Workbooks("Two-Phase Envelope on a PV Diagram.xlsm").Worksheets("PV Diagram").Cells(6 + 3 * row, 5).Value
                .Cells(12 + row, 5).Value = Workbooks("Two-Phase Envelope on a PV Diagram.xlsm").Worksheets("PV Diagram").Cells(6 + 3 * row, 6).Value
                .Cells(12 + row, 6).Value = Workbooks("Two-Phase Envelope on a PV Diagram.xlsm").Worksheets("PV Diagram").Cells(6 + 3 * row, 7).Value
                .Cells(12 + row, 7).Value = Workbooks("Two-Phase Envelope on a PH Diagram.xlsm").Worksheets("PH Diagram").Cells(10 + 3 * row, 6).Value
                .Cells(12 + row, 8).Value = Workbooks("Two-Phase Envelope on a PH Diagram.xlsm").Worksheets("PH Diagram").Cells(10 + 3 * row, 7).Value
                .Cells(12 + row, 9).Value = Workbooks("Two-Phase Envelope on a PS Diagram.xlsm").Worksheets("PS Diagram").Cells(10 + 3 * row, 6).Value
                .Cells(12 + row, 10).Value = Workbooks("Two-Phase Envelope on a PS Diagram.xlsm").Worksheets("PS Diagram").Cells(10 + 3 * row, 7).Value
                row = row + 1
            Wend
            row_data = row
            ' Format
            .Range(Cells(12, 1), Cells(11 + row_data, 10)).Select
            With Selection
                .HorizontalAlignment = xlCenter
                .VerticalAlignment = xlBottom
                .WrapText = False
                .Orientation = 0
                .AddIndent = False
                .IndentLevel = 0
                .ShrinkToFit = False
                .ReadingOrder = xlContext
                .MergeCells = False
            End With
            With Selection
                .HorizontalAlignment = xlCenter
                .VerticalAlignment = xlCenter
                .WrapText = False
                .Orientation = 0
                .AddIndent = False
                .IndentLevel = 0
                .ShrinkToFit = False
                .ReadingOrder = xlContext
                .MergeCells = False
            End With
            Selection.Borders(xlDiagonalDown).LineStyle = xlNone
            Selection.Borders(xlDiagonalUp).LineStyle = xlNone
            With Selection.Borders(xlEdgeLeft)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeTop)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeBottom)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeRight)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlInsideVertical)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlThin
            End With
            With Selection.Borders(xlInsideHorizontal)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlThin
            End With
            .Range(Cells(11, 1), Cells(11 + row_data, 1)).Select
            Selection.Borders(xlDiagonalDown).LineStyle = xlNone
            Selection.Borders(xlDiagonalUp).LineStyle = xlNone
            With Selection.Borders(xlEdgeLeft)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeTop)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeBottom)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeRight)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            Selection.Borders(xlInsideVertical).LineStyle = xlNone
            ' Formulas of "EXACT DATA OR LINEAR INTERPOLATION" section
            .Range("L13").Formula2R1C1 = "=IF(R[1]C[0]="""",""-"",MAX(IF(R[-1]C[-11]:R[" & row_data - 2 & "]C[-11]<=R[1]C[0],R[-1]C[-11]:R[" & row_data - 2 & "]C[-11])))"
            .Range("M13").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-1]C[-12]:R[" & row_data - 2 & "]C[-3],2,FALSE),""-"")"
            .Range("N13").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-1]C[-13]:R[" & row_data - 2 & "]C[-4],5,FALSE),""-"")"
            .Range("O13").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-1]C[-14]:R[" & row_data - 2 & "]C[-5],6,FALSE),""-"")"
            .Range("P13").Formula2R1C1 = "=IF(R[0]C[-4]<>""-"",VLOOKUP(R[0]C[-4],R[-1]C[-15]:R[" & row_data - 2 & "]C[-6],7,FALSE),""-"")"
            .Range("Q13").Formula2R1C1 = "=IF(R[0]C[-5]<>""-"",VLOOKUP(R[0]C[-5],R[-1]C[-16]:R[" & row_data - 2 & "]C[-7],8,FALSE),""-"")"
            .Range("R13").Formula2R1C1 = "=IF(R[0]C[-6]<>""-"",VLOOKUP(R[0]C[-6],R[-1]C[-17]:R[" & row_data - 2 & "]C[-8],9,FALSE),""-"")"
            .Range("S13").Formula2R1C1 = "=IF(R[0]C[-7]<>""-"",VLOOKUP(R[0]C[-7],R[-1]C[-18]:R[" & row_data - 2 & "]C[-9],10,FALSE),""-"")"
            .Range("L15").Formula2R1C1 = "=IF(R[-1]C[0]="""",""-"",MIN(IF(R[-3]C[-11]:R[" & row_data - 4 & "]C[-11]>=R[-1]C[0],R[-3]C[-11]:R[" & row_data - 4 & "]C[-11])))"
            .Range("M15").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-3]C[-12]:R[" & row_data - 4 & "]C[-3],2,FALSE),""-"")"
            .Range("N15").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-3]C[-13]:R[" & row_data - 4 & "]C[-4],5,FALSE),""-"")"
            .Range("O15").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-3]C[-14]:R[" & row_data - 4 & "]C[-5],6,FALSE),""-"")"
            .Range("P15").Formula2R1C1 = "=IF(R[0]C[-4]<>""-"",VLOOKUP(R[0]C[-4],R[-3]C[-15]:R[" & row_data - 4 & "]C[-6],7,FALSE),""-"")"
            .Range("Q15").Formula2R1C1 = "=IF(R[0]C[-5]<>""-"",VLOOKUP(R[0]C[-5],R[-3]C[-16]:R[" & row_data - 4 & "]C[-7],8,FALSE),""-"")"
            .Range("R15").Formula2R1C1 = "=IF(R[0]C[-6]<>""-"",VLOOKUP(R[0]C[-6],R[-3]C[-17]:R[" & row_data - 4 & "]C[-8],9,FALSE),""-"")"
            .Range("S15").Formula2R1C1 = "=IF(R[0]C[-7]<>""-"",VLOOKUP(R[0]C[-7],R[-3]C[-18]:R[" & row_data - 4 & "]C[-9],10,FALSE),""-"")"
            .Range("L14").Select
            With Selection.Validation
                .Delete
                .Add Type:=xlValidateDecimal, AlertStyle:=xlValidAlertStop, Operator _
                :=xlBetween, Formula1:="=MIN(A12:A" & 11 + row_data & ")", Formula2:="=MAX(A12:A" & 11 + row_data & ")"
                .IgnoreBlank = True
                .InCellDropdown = True
                .InputTitle = ""
                .ErrorTitle = ""
                .InputMessage = ""
                .ErrorMessage = ""
                .ShowInput = True
                .ShowError = True
            End With
            .Range("P18").Select
            With Selection.Validation
                .Delete
                .Add Type:=xlValidateCustom, AlertStyle:=xlValidAlertStop, Operator:= _
                xlBetween, Formula1:="=ISNUMBER(P18)"
                .IgnoreBlank = True
                .InCellDropdown = True
                .InputTitle = ""
                .ErrorTitle = ""
                .InputMessage = ""
                .ErrorMessage = ""
                .ShowInput = True
                .ShowError = True
            End With
            .Columns("A:S").EntireColumn.AutoFit
            .Columns("C:D").ColumnWidth = 9.71
            .Columns("K:K").ColumnWidth = 9.71
            .Range("A3").Select
        End With
    Else
        With Workbooks("Two Phases in Equilibrium.xlsm").Worksheets("Temperature")
            ' Check if it is possible to use experimental data
            If .Range("B3") = "" Then
                MsgBox "The value of COMPOUND is empty.", vbExclamation
                Exit Sub
            End If
            If .Range("A12") = "" Then
                MsgBox "No experimental data presented.", vbExclamation
                Exit Sub
            End If
            .Range("B4:B9").Value = "-"
            row = 0
            While .Cells(12 + row, 1) <> ""
                row = row + 1
            Wend
            row_data = row
            ' Format
            .Range(Cells(12, 1), Cells(11 + row_data, 10)).Select
            With Selection
                .HorizontalAlignment = xlCenter
                .VerticalAlignment = xlBottom
                .WrapText = False
                .Orientation = 0
                .AddIndent = False
                .IndentLevel = 0
                .ShrinkToFit = False
                .ReadingOrder = xlContext
                .MergeCells = False
            End With
            With Selection
                .HorizontalAlignment = xlCenter
                .VerticalAlignment = xlCenter
                .WrapText = False
                .Orientation = 0
                .AddIndent = False
                .IndentLevel = 0
                .ShrinkToFit = False
                .ReadingOrder = xlContext
                .MergeCells = False
            End With
            Selection.Borders(xlDiagonalDown).LineStyle = xlNone
            Selection.Borders(xlDiagonalUp).LineStyle = xlNone
            With Selection.Borders(xlEdgeLeft)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeTop)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeBottom)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeRight)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlInsideVertical)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlThin
            End With
            With Selection.Borders(xlInsideHorizontal)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlThin
            End With
            .Range(Cells(11, 1), Cells(11 + row_data, 1)).Select
            Selection.Borders(xlDiagonalDown).LineStyle = xlNone
            Selection.Borders(xlDiagonalUp).LineStyle = xlNone
            With Selection.Borders(xlEdgeLeft)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeTop)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeBottom)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeRight)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            Selection.Borders(xlInsideVertical).LineStyle = xlNone
            ' Formulas of "EXACT DATA OR LINEAR INTERPOLATION" section
            .Range("L13").Formula2R1C1 = "=IF(R[1]C[0]="""",""-"",MAX(IF(R[-1]C[-11]:R[" & row_data - 2 & "]C[-11]<=R[1]C[0],R[-1]C[-11]:R[" & row_data - 2 & "]C[-11])))"
            .Range("M13").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-1]C[-12]:R[" & row_data - 2 & "]C[-3],2,FALSE),""-"")"
            .Range("N13").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-1]C[-13]:R[" & row_data - 2 & "]C[-4],5,FALSE),""-"")"
            .Range("O13").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-1]C[-14]:R[" & row_data - 2 & "]C[-5],6,FALSE),""-"")"
            .Range("P13").Formula2R1C1 = "=IF(R[0]C[-4]<>""-"",VLOOKUP(R[0]C[-4],R[-1]C[-15]:R[" & row_data - 2 & "]C[-6],7,FALSE),""-"")"
            .Range("Q13").Formula2R1C1 = "=IF(R[0]C[-5]<>""-"",VLOOKUP(R[0]C[-5],R[-1]C[-16]:R[" & row_data - 2 & "]C[-7],8,FALSE),""-"")"
            .Range("R13").Formula2R1C1 = "=IF(R[0]C[-6]<>""-"",VLOOKUP(R[0]C[-6],R[-1]C[-17]:R[" & row_data - 2 & "]C[-8],9,FALSE),""-"")"
            .Range("S13").Formula2R1C1 = "=IF(R[0]C[-7]<>""-"",VLOOKUP(R[0]C[-7],R[-1]C[-18]:R[" & row_data - 2 & "]C[-9],10,FALSE),""-"")"
            .Range("L15").Formula2R1C1 = "=IF(R[-1]C[0]="""",""-"",MIN(IF(R[-3]C[-11]:R[" & row_data - 4 & "]C[-11]>=R[-1]C[0],R[-3]C[-11]:R[" & row_data - 4 & "]C[-11])))"
            .Range("M15").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-3]C[-12]:R[" & row_data - 4 & "]C[-3],2,FALSE),""-"")"
            .Range("N15").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-3]C[-13]:R[" & row_data - 4 & "]C[-4],5,FALSE),""-"")"
            .Range("O15").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-3]C[-14]:R[" & row_data - 4 & "]C[-5],6,FALSE),""-"")"
            .Range("P15").Formula2R1C1 = "=IF(R[0]C[-4]<>""-"",VLOOKUP(R[0]C[-4],R[-3]C[-15]:R[" & row_data - 4 & "]C[-6],7,FALSE),""-"")"
            .Range("Q15").Formula2R1C1 = "=IF(R[0]C[-5]<>""-"",VLOOKUP(R[0]C[-5],R[-3]C[-16]:R[" & row_data - 4 & "]C[-7],8,FALSE),""-"")"
            .Range("R15").Formula2R1C1 = "=IF(R[0]C[-6]<>""-"",VLOOKUP(R[0]C[-6],R[-3]C[-17]:R[" & row_data - 4 & "]C[-8],9,FALSE),""-"")"
            .Range("S15").Formula2R1C1 = "=IF(R[0]C[-7]<>""-"",VLOOKUP(R[0]C[-7],R[-3]C[-18]:R[" & row_data - 4 & "]C[-9],10,FALSE),""-"")"
            .Range("L14").Select
            With Selection.Validation
                .Delete
                .Add Type:=xlValidateDecimal, AlertStyle:=xlValidAlertStop, Operator _
                :=xlBetween, Formula1:="=MIN(A12:A" & 11 + row_data & ")", Formula2:="=MAX(A12:A" & 11 + row_data & ")"
                .IgnoreBlank = True
                .InCellDropdown = True
                .InputTitle = ""
                .ErrorTitle = ""
                .InputMessage = ""
                .ErrorMessage = ""
                .ShowInput = True
                .ShowError = True
            End With
            .Range("P18").Select
            With Selection.Validation
                .Delete
                .Add Type:=xlValidateCustom, AlertStyle:=xlValidAlertStop, Operator:= _
                xlBetween, Formula1:="=ISNUMBER(P18)"
                .IgnoreBlank = True
                .InCellDropdown = True
                .InputTitle = ""
                .ErrorTitle = ""
                .InputMessage = ""
                .ErrorMessage = ""
                .ShowInput = True
                .ShowError = True
            End With
            .Columns("A:S").EntireColumn.AutoFit
            .Columns("C:D").ColumnWidth = 9.71
            .Columns("K:K").ColumnWidth = 9.71
            .Range("A3").Select
        End With
    End If
    FUGACITY_TEST.Enabled = False
    EXPERIMENTAL_DATA.Enabled = False
    COMPUTE.Enabled = False
    CLEAN.Enabled = True
End Sub
```